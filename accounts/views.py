from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .models import User


@login_required
def user_list(request):
    if not request.user.can_manage_users():
        messages.error(request, 'You do not have permission to manage users.')
        return redirect('dashboard')
    
    users = User.objects.all().order_by('-created_at')
    context = {'users': users}
    return render(request, 'accounts/user_list.html', context)


@login_required
def user_create(request):
    if not request.user.can_manage_users():
        messages.error(request, 'You do not have permission to create users.')
        return redirect('dashboard')
    
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')
        role = request.POST.get('role', 'viewer')
        
        # Validate required fields
        if not username or not password:
            messages.error(request, 'Username and password are required.')
            return render(request, 'accounts/user_create.html')
        
        # Check if username already exists
        if User.objects.filter(username=username).exists():
            messages.error(request, f'Username "{username}" already exists. Please choose a different username.')
            return render(request, 'accounts/user_create.html')
        
        # Check if email already exists (if provided)
        if email and User.objects.filter(email=email).exists():
            messages.error(request, f'Email "{email}" is already in use. Please use a different email.')
            return render(request, 'accounts/user_create.html')
        
        try:
            user = User.objects.create_user(
                username=username,
                email=email,
                password=password,
                role=role
            )
            
            messages.success(request, f'User "{username}" created successfully!')
            return redirect('user_list')
        except Exception as e:
            messages.error(request, f'Error creating user: {str(e)}')
            return render(request, 'accounts/user_create.html')
    
    return render(request, 'accounts/user_create.html')


@login_required
def user_edit(request, user_id):
    if not request.user.can_manage_users():
        messages.error(request, 'You do not have permission to edit users.')
        return redirect('dashboard')
    
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        email = request.POST.get('email', user.email)
        role = request.POST.get('role', user.role)
        is_active = request.POST.get('is_active') == 'on'
        
        # Check if email is being changed and if it's already in use
        if email != user.email and User.objects.filter(email=email).exclude(id=user_id).exists():
            messages.error(request, f'Email "{email}" is already in use by another user.')
            context = {'user_obj': user}
            return render(request, 'accounts/user_edit.html', context)
        
        try:
            user.email = email
            user.role = role
            user.is_active = is_active
            user.save()
            
            messages.success(request, f'User "{user.username}" updated successfully!')
            return redirect('user_list')
        except Exception as e:
            messages.error(request, f'Error updating user: {str(e)}')
            context = {'user_obj': user}
            return render(request, 'accounts/user_edit.html', context)
    
    context = {'user_obj': user}
    return render(request, 'accounts/user_edit.html', context)


@login_required
def user_delete(request, user_id):
    if not request.user.can_manage_users():
        messages.error(request, 'You do not have permission to delete users.')
        return redirect('dashboard')
    
    user = get_object_or_404(User, id=user_id)
    
    if request.method == 'POST':
        username = user.username
        user.delete()
        messages.success(request, f'User "{username}" deleted successfully!')
        return redirect('user_list')
    
    context = {'user_obj': user}
    return render(request, 'accounts/user_confirm_delete.html', context)
