from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.http import JsonResponse
from django.views.decorators.http import require_http_methods
from .models import Device
from messaging.models import Message


@login_required
def device_list(request):
    """Display all devices"""
    devices = Device.objects.all()
    
    context = {
        'devices': devices,
        'total_devices': devices.count(),
        'online_devices': devices.filter(status='online').count(),
        'offline_devices': devices.filter(status='offline').count(),
    }
    return render(request, 'devices/device_list.html', context)


@login_required
def device_detail(request, device_id):
    """Display device details"""
    device = get_object_or_404(Device, id=device_id)
    messages_list = Message.objects.filter(device=device).order_by('-created_at')[:50]
    
    # Get server URL for agent configuration
    server_url = request.build_absolute_uri('/').rstrip('/')
    # Convert http to ws, https to wss
    if server_url.startswith('https://'):
        server_url = server_url.replace('https://', 'wss://')
    else:
        server_url = server_url.replace('http://', 'ws://')
    
    context = {
        'device': device,
        'messages': messages_list,
        'server_url': server_url,
    }
    return render(request, 'devices/device_detail.html', context)


@login_required
def device_create(request):
    """Create a new device"""
    if request.method == 'POST':
        device_name = request.POST.get('device_name')
        operating_system = request.POST.get('operating_system', 'Unknown')
        
        device = Device.objects.create(
            device_name=device_name,
            operating_system=operating_system
        )
        
        messages.success(request, f'Device "{device_name}" created successfully!')
        return redirect('device_detail', device_id=device.id)
    
    return render(request, 'devices/device_create.html')


@login_required
def device_delete(request, device_id):
    """Delete a device"""
    device = get_object_or_404(Device, id=device_id)
    
    if request.method == 'POST':
        device_name = device.device_name
        device.delete()
        messages.success(request, f'Device "{device_name}" deleted successfully!')
        return redirect('device_list')
    
    return render(request, 'devices/device_confirm_delete.html', {'device': device})


@login_required
@require_http_methods(["GET"])
def device_status_api(request):
    """API endpoint for device status"""
    devices = Device.objects.all()
    
    data = {
        'total': devices.count(),
        'online': devices.filter(status='online').count(),
        'offline': devices.filter(status='offline').count(),
        'devices': [
            {
                'id': device.id,
                'name': device.device_name,
                'status': device.status,
                'os': device.operating_system,
                'last_seen': device.last_seen.isoformat(),
            }
            for device in devices
        ]
    }
    
    return JsonResponse(data)
