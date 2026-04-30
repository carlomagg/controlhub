#!/usr/bin/env python3
"""
ControlHub Live - Client Agent
Remote monitoring and management agent for ControlHub Live platform
"""

import os
import sys
import json
import time
import base64
import socket
import platform
import threading
import logging
from io import BytesIO
from datetime import datetime

try:
    import websocket
    import mss
    from PIL import Image
    import requests
except ImportError:
    print("ERROR: Required packages not installed!")
    print("Please install: pip install websocket-client mss pillow requests")
    sys.exit(1)

try:
    import tkinter as tk
    from tkinter import messagebox
    TKINTER_AVAILABLE = True
except ImportError:
    TKINTER_AVAILABLE = False
    print("WARNING: tkinter not available. Message notifications will be disabled.")

# Configuration
CONFIG_FILE = 'agent_config.json'
DEFAULT_CONFIG = {
    'server_url': 'ws://localhost:8000',
    'device_token': '',
    'device_name': socket.gethostname(),
    'capture_interval': 0.5,  # seconds between captures
    'jpeg_quality': 60,
    'screen_width': 1280,
    'reconnect_delay': 5,
}

# Logging setup
logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s',
    handlers=[
        logging.FileHandler('agent.log'),
        logging.StreamHandler()
    ]
)
logger = logging.getLogger(__name__)


class ControlHubAgent:
    """Main agent class for ControlHub Live"""
    
    def __init__(self, config):
        self.config = config
        self.ws = None
        self.running = False
        self.connected = False
        self.capture_thread = None
        self.heartbeat_thread = None
        
        # Validate configuration
        if not self.config.get('device_token'):
            logger.error("Device token not configured!")
            raise ValueError("Device token is required. Please configure agent_config.json")
        
        logger.info(f"Initializing ControlHub Agent for device: {self.config['device_name']}")
    
    def get_system_info(self):
        """Collect system information"""
        try:
            import psutil
            cpu_info = f"{psutil.cpu_count()} cores"
            ram_total = f"{psutil.virtual_memory().total / (1024**3):.1f} GB"
        except ImportError:
            cpu_info = "N/A"
            ram_total = "N/A"
        
        try:
            with mss.mss() as sct:
                monitor = sct.monitors[1]
                screen_resolution = f"{monitor['width']}x{monitor['height']}"
        except Exception:
            screen_resolution = "N/A"
        
        return {
            'type': 'system_info',
            'hostname': socket.gethostname(),
            'ip_address': self.get_local_ip(),
            'cpu_info': cpu_info,
            'ram_total': ram_total,
            'screen_resolution': screen_resolution,
        }
    
    def get_local_ip(self):
        """Get local IP address"""
        try:
            s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            s.connect(("8.8.8.8", 80))
            ip = s.getsockname()[0]
            s.close()
            return ip
        except Exception:
            return "127.0.0.1"
    
    def capture_screen(self):
        """Capture and compress screen"""
        try:
            with mss.mss() as sct:
                monitor = sct.monitors[1]  # Primary monitor
                screenshot = sct.grab(monitor)
                
                # Convert to PIL Image
                img = Image.frombytes('RGB', screenshot.size, screenshot.rgb)
                
                # Resize if needed
                if img.width > self.config['screen_width']:
                    ratio = self.config['screen_width'] / img.width
                    new_height = int(img.height * ratio)
                    img = img.resize((self.config['screen_width'], new_height), Image.LANCZOS)
                
                # Compress to JPEG
                buffer = BytesIO()
                img.save(buffer, format='JPEG', quality=self.config['jpeg_quality'], optimize=True)
                
                # Encode to base64
                img_base64 = base64.b64encode(buffer.getvalue()).decode('utf-8')
                
                return img_base64
        
        except Exception as e:
            logger.error(f"Screen capture error: {e}")
            return None
    
    def screen_capture_loop(self):
        """Continuous screen capture and streaming"""
        logger.info("Screen capture loop started")
        
        while self.running and self.connected:
            try:
                frame = self.capture_screen()
                
                if frame and self.ws:
                    self.ws.send(json.dumps({
                        'type': 'screen_frame',
                        'frame': frame,
                        'timestamp': datetime.now().isoformat(),
                    }))
                
                time.sleep(self.config['capture_interval'])
            
            except Exception as e:
                logger.error(f"Capture loop error: {e}")
                time.sleep(1)
        
        logger.info("Screen capture loop stopped")
    
    def heartbeat_loop(self):
        """Send periodic heartbeat to server"""
        logger.info("Heartbeat loop started")
        
        while self.running and self.connected:
            try:
                if self.ws:
                    self.ws.send(json.dumps({'type': 'heartbeat'}))
                time.sleep(30)  # Every 30 seconds
            except Exception as e:
                logger.error(f"Heartbeat error: {e}")
                break
        
        logger.info("Heartbeat loop stopped")
    
    def show_message_notification(self, message, sender):
        """Show message notification popup"""
        if not TKINTER_AVAILABLE:
            logger.info(f"Message from {sender}: {message}")
            return
        
        try:
            root = tk.Tk()
            root.withdraw()
            messagebox.showinfo(
                f"Message from {sender}",
                message
            )
            root.destroy()
        except Exception as e:
            logger.error(f"Notification error: {e}")
    
    def on_message(self, ws, message):
        """Handle incoming WebSocket messages"""
        try:
            data = json.loads(message)
            msg_type = data.get('type')
            
            if msg_type == 'message':
                # Received message from admin
                msg_text = data.get('message')
                sender = data.get('sender')
                message_id = data.get('message_id')
                
                logger.info(f"Received message from {sender}: {msg_text}")
                
                # Show notification
                threading.Thread(
                    target=self.show_message_notification,
                    args=(msg_text, sender),
                    daemon=True
                ).start()
                
                # Mark as delivered
                self.ws.send(json.dumps({
                    'type': 'message_delivered',
                    'message_id': message_id,
                }))
            
            elif msg_type == 'heartbeat_ack':
                pass  # Heartbeat acknowledged
            
            else:
                logger.debug(f"Unknown message type: {msg_type}")
        
        except Exception as e:
            logger.error(f"Message handling error: {e}")
    
    def on_error(self, ws, error):
        """Handle WebSocket errors"""
        logger.error(f"WebSocket error: {error}")
    
    def on_close(self, ws, close_status_code, close_msg):
        """Handle WebSocket connection close"""
        logger.warning(f"WebSocket closed: {close_status_code} - {close_msg}")
        self.connected = False
    
    def on_open(self, ws):
        """Handle WebSocket connection open"""
        logger.info("WebSocket connected successfully!")
        self.connected = True
        
        # Send system information
        system_info = self.get_system_info()
        self.ws.send(json.dumps(system_info))
        
        # Start capture thread
        self.capture_thread = threading.Thread(target=self.screen_capture_loop, daemon=True)
        self.capture_thread.start()
        
        # Start heartbeat thread
        self.heartbeat_thread = threading.Thread(target=self.heartbeat_loop, daemon=True)
        self.heartbeat_thread.start()
    
    def connect(self):
        """Connect to ControlHub server"""
        ws_url = f"{self.config['server_url']}/ws/device/{self.config['device_token']}/"
        
        logger.info(f"Connecting to: {ws_url}")
        
        self.ws = websocket.WebSocketApp(
            ws_url,
            on_open=self.on_open,
            on_message=self.on_message,
            on_error=self.on_error,
            on_close=self.on_close
        )
        
        self.running = True
        
        # Run WebSocket in a loop with auto-reconnect
        while self.running:
            try:
                self.ws.run_forever()
            except Exception as e:
                logger.error(f"Connection error: {e}")
            
            if self.running:
                logger.info(f"Reconnecting in {self.config['reconnect_delay']} seconds...")
                time.sleep(self.config['reconnect_delay'])
    
    def stop(self):
        """Stop the agent"""
        logger.info("Stopping agent...")
        self.running = False
        self.connected = False
        
        if self.ws:
            self.ws.close()
        
        logger.info("Agent stopped")


def load_config():
    """Load configuration from file"""
    if os.path.exists(CONFIG_FILE):
        try:
            with open(CONFIG_FILE, 'r') as f:
                config = json.load(f)
                logger.info("Configuration loaded from file")
                return {**DEFAULT_CONFIG, **config}
        except Exception as e:
            logger.error(f"Error loading config: {e}")
    
    # Create default config file
    with open(CONFIG_FILE, 'w') as f:
        json.dump(DEFAULT_CONFIG, f, indent=4)
    
    logger.info("Default configuration created. Please edit agent_config.json")
    return DEFAULT_CONFIG


def main():
    """Main entry point"""
    print("=" * 60)
    print("ControlHub Live - Client Agent")
    print("Remote Monitoring & Management")
    print("=" * 60)
    print()
    
    # Load configuration
    config = load_config()
    
    if not config.get('device_token'):
        print("\nERROR: Device token not configured!")
        print("Please edit 'agent_config.json' and add your device token.")
        print("You can get the token from the ControlHub dashboard after creating a device.")
        return
    
    print(f"Device Name: {config['device_name']}")
    print(f"Server URL: {config['server_url']}")
    print(f"Capture Interval: {config['capture_interval']}s")
    print()
    
    # Create and start agent
    try:
        agent = ControlHubAgent(config)
        agent.connect()
    except KeyboardInterrupt:
        print("\n\nShutting down...")
        if 'agent' in locals():
            agent.stop()
    except Exception as e:
        logger.error(f"Fatal error: {e}")
        sys.exit(1)


if __name__ == '__main__':
    main()
