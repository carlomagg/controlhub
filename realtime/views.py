from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from devices.models import Device


@login_required
def live_monitor(request, device_id):
    """Live screen monitoring page"""
    device = get_object_or_404(Device, id=device_id)
    
    if not request.user.can_monitor_devices() and request.user.role != 'viewer':
        messages.error(request, 'You do not have permission to monitor devices.')
        return redirect('dashboard')
    
    context = {
        'device': device,
        'can_send_messages': request.user.can_send_messages(),
    }
    return render(request, 'realtime/live_monitor.html', context)


@login_required
def dashboard(request):
    """Main dashboard"""
    from messaging.models import Message
    from datetime import datetime, timedelta
    from django.utils import timezone
    
    devices = Device.objects.all()
    recent_messages = Message.objects.all().order_by('-created_at')[:10]
    
    # Calculate messages today
    today = timezone.now().date()
    messages_today = Message.objects.filter(created_at__date=today).count()
    
    # Get all users
    from accounts.models import User
    all_users = User.objects.all()
    
    # Use enhanced admin dashboard for super admins and admins
    if request.user.role in ['super_admin', 'admin']:
        context = {
            'total_devices': devices.count(),
            'online_devices': devices.filter(status='online').count(),
            'offline_devices': devices.filter(status='offline').count(),
            'devices': devices,
            'total_users': all_users.count(),
            'active_users': all_users.filter(is_active=True).count(),
            'users': all_users,
            'total_messages': Message.objects.count(),
            'messages_today': messages_today,
            'recent_messages': recent_messages,
            'user': request.user,
        }
        return render(request, 'realtime/admin_dashboard.html', context)
    
    # Regular dashboard for other users
    context = {
        'total_devices': devices.count(),
        'online_devices': devices.filter(status='online').count(),
        'offline_devices': devices.filter(status='offline').count(),
        'recent_devices': devices[:5],
        'recent_messages': recent_messages,
        'user': request.user,
    }
    return render(request, 'realtime/dashboard.html', context)
