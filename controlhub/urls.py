"""
URL configuration for controlhub project.
"""
from django.contrib import admin
from django.urls import path, include
from django.conf import settings
from django.conf.urls.static import static
from django.shortcuts import redirect

urlpatterns = [
    path('', lambda request: redirect('dashboard')),
    path('admin/', admin.site.urls),
    path('accounts/', include('accounts.urls')),
    path('devices/', include('devices.urls')),
    path('messaging/', include('messaging.urls')),
    path('dashboard/', include('realtime.urls')),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
    urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
