from django.urls import re_path
from . import consumers

websocket_urlpatterns = [
    re_path(r'ws/device/(?P<device_token>[^/]+)/$', consumers.DeviceConsumer.as_asgi()),
    re_path(r'ws/monitor/(?P<device_id>\d+)/$', consumers.MonitorConsumer.as_asgi()),
]
