from django.contrib import admin
from .models import Message


@admin.register(Message)
class MessageAdmin(admin.ModelAdmin):
    list_display = ['device', 'sender', 'message_preview', 'delivered', 'read', 'created_at']
    list_filter = ['delivered', 'read', 'created_at']
    search_fields = ['message', 'device__device_name', 'sender__username']
    readonly_fields = ['created_at']
    
    def message_preview(self, obj):
        return obj.message[:50] + '...' if len(obj.message) > 50 else obj.message
    message_preview.short_description = 'Message'
