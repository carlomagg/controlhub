from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages as django_messages
from django.http import JsonResponse
from channels.layers import get_channel_layer
from asgiref.sync import async_to_sync
from devices.models import Device
from .models import Message


@login_required
def send_message(request, device_id):
    """Send a message to a device"""
    if not request.user.can_send_messages():
        django_messages.error(request, 'You do not have permission to send messages.')
        return redirect('device_detail', device_id=device_id)
    
    device = get_object_or_404(Device, id=device_id)
    
    if request.method == 'POST':
        message_text = request.POST.get('message')
        
        if message_text:
            message = Message.objects.create(
                device=device,
                sender=request.user,
                message=message_text
            )
            
            # Send message via WebSocket
            channel_layer = get_channel_layer()
            async_to_sync(channel_layer.group_send)(
                f'device_{device.unique_token}',
                {
                    'type': 'device_message',
                    'message': message_text,
                    'message_id': message.id,
                    'sender': request.user.username,
                }
            )
            
            django_messages.success(request, 'Message sent successfully!')
        
        return redirect('device_detail', device_id=device_id)
    
    return render(request, 'messaging/send_message.html', {'device': device})


@login_required
def message_history(request, device_id):
    """View message history for a device"""
    device = get_object_or_404(Device, id=device_id)
    message_list = Message.objects.filter(device=device).order_by('-created_at')
    
    context = {
        'device': device,
        'messages': message_list,
    }
    return render(request, 'messaging/message_history.html', context)
