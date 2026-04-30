from django.urls import path
from . import views

urlpatterns = [
    path('', views.dashboard, name='dashboard'),
    path('monitor/<int:device_id>/', views.live_monitor, name='live_monitor'),
]
