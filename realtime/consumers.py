import json
import base64
from channels.generic.websocket import AsyncWebsocketConsumer
from channels.db import database_sync_to_async
from devices.models import Device
from messaging.models import Message


class DeviceConsumer(AsyncWebsocketConsumer):
    """WebSocket consumer for device agents"""
    
    async def connect(self):
        self.device_token = self.scope['url_route']['kwargs']['device_token']
        self.device = await self.get_device(self.device_token)
        
        if not self.device:
            await self.close()
            return
        
        self.device_group_name = f'device_{self.device_token}'
        
        # Join device group
        await self.channel_layer.group_add(
            self.device_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Mark device as online
        await self.set_device_online()
        
        # Notify monitors
        await self.channel_layer.group_send(
            f'monitor_{self.device.id}',
            {
                'type': 'device_status',
                'status': 'online',
                'device_id': self.device.id,
            }
        )
    
    async def disconnect(self, close_code):
        if hasattr(self, 'device') and self.device:
            # Mark device as offline
            await self.set_device_offline()
            
            # Notify monitors
            await self.channel_layer.group_send(
                f'monitor_{self.device.id}',
                {
                    'type': 'device_status',
                    'status': 'offline',
                    'device_id': self.device.id,
                }
            )
            
            # Leave device group
            await self.channel_layer.group_discard(
                self.device_group_name,
                self.channel_name
            )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get('type')
        
        if message_type == 'heartbeat':
            await self.update_device_last_seen()
            await self.send(text_data=json.dumps({'type': 'heartbeat_ack'}))
        
        elif message_type == 'screen_frame':
            # Forward screen frame to monitors
            await self.channel_layer.group_send(
                f'monitor_{self.device.id}',
                {
                    'type': 'screen_frame',
                    'frame': data.get('frame'),
                    'device_id': self.device.id,
                }
            )
        
        elif message_type == 'message_delivered':
            message_id = data.get('message_id')
            await self.mark_message_delivered(message_id)
        
        elif message_type == 'message_read':
            message_id = data.get('message_id')
            await self.mark_message_read(message_id)
        
        elif message_type == 'system_info':
            await self.update_device_info(data)
    
    async def device_message(self, event):
        """Send message to device"""
        await self.send(text_data=json.dumps({
            'type': 'message',
            'message': event['message'],
            'message_id': event['message_id'],
            'sender': event['sender'],
        }))
    
    @database_sync_to_async
    def get_device(self, token):
        try:
            return Device.objects.get(unique_token=token)
        except Device.DoesNotExist:
            return None
    
    @database_sync_to_async
    def set_device_online(self):
        self.device.set_online()
    
    @database_sync_to_async
    def set_device_offline(self):
        self.device.set_offline()
    
    @database_sync_to_async
    def update_device_last_seen(self):
        self.device.update_last_seen()
    
    @database_sync_to_async
    def mark_message_delivered(self, message_id):
        try:
            message = Message.objects.get(id=message_id)
            message.mark_delivered()
        except Message.DoesNotExist:
            pass
    
    @database_sync_to_async
    def mark_message_read(self, message_id):
        try:
            message = Message.objects.get(id=message_id)
            message.mark_read()
        except Message.DoesNotExist:
            pass
    
    @database_sync_to_async
    def update_device_info(self, data):
        if 'ip_address' in data:
            self.device.ip_address = data['ip_address']
        if 'hostname' in data:
            self.device.hostname = data['hostname']
        if 'cpu_info' in data:
            self.device.cpu_info = data['cpu_info']
        if 'ram_total' in data:
            self.device.ram_total = data['ram_total']
        if 'screen_resolution' in data:
            self.device.screen_resolution = data['screen_resolution']
        self.device.save()



class MonitorConsumer(AsyncWebsocketConsumer):
    """WebSocket consumer for admin monitors"""
    
    async def connect(self):
        self.device_id = self.scope['url_route']['kwargs']['device_id']
        self.monitor_group_name = f'monitor_{self.device_id}'
        
        # Join monitor group
        await self.channel_layer.group_add(
            self.monitor_group_name,
            self.channel_name
        )
        
        await self.accept()
        
        # Send current device status
        device = await self.get_device()
        if device:
            await self.send(text_data=json.dumps({
                'type': 'device_status',
                'status': device.status,
                'device_id': device.id,
            }))
    
    async def disconnect(self, close_code):
        # Leave monitor group
        await self.channel_layer.group_discard(
            self.monitor_group_name,
            self.channel_name
        )
    
    async def receive(self, text_data):
        data = json.loads(text_data)
        message_type = data.get('type')
        
        if message_type == 'request_frame':
            # Request a frame from the device
            device = await self.get_device()
            if device:
                await self.channel_layer.group_send(
                    f'device_{device.unique_token}',
                    {
                        'type': 'request_screen_frame',
                    }
                )
    
    async def screen_frame(self, event):
        """Forward screen frame to monitor"""
        await self.send(text_data=json.dumps({
            'type': 'screen_frame',
            'frame': event['frame'],
            'device_id': event['device_id'],
        }))
    
    async def device_status(self, event):
        """Forward device status to monitor"""
        await self.send(text_data=json.dumps({
            'type': 'device_status',
            'status': event['status'],
            'device_id': event['device_id'],
        }))
    
    @database_sync_to_async
    def get_device(self):
        try:
            return Device.objects.get(id=self.device_id)
        except Device.DoesNotExist:
            return None
