from django.contrib import admin
from .models import Device


@admin.register(Device)
class DeviceAdmin(admin.ModelAdmin):
    list_display = ['device_name', 'operating_system', 'status', 'ip_address', 'last_seen', 'created_at']
    list_filter = ['status', 'operating_system', 'created_at']
    search_fields = ['device_name', 'hostname', 'ip_address', 'unique_token']
    readonly_fields = ['unique_token', 'created_at', 'last_seen']
    
    fieldsets = (
        ('Device Information', {
            'fields': ('device_name', 'unique_token', 'operating_system', 'hostname')
        }),
        ('Network & Status', {
            'fields': ('ip_address', 'status', 'last_seen')
        }),
        ('System Information', {
            'fields': ('cpu_info', 'ram_total', 'screen_resolution')
        }),
        ('Timestamps', {
            'fields': ('created_at',)
        }),
    )
