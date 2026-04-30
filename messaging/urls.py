from django.urls import path
from . import views

urlpatterns = [
    path('send/<int:device_id>/', views.send_message, name='send_message'),
    path('history/<int:device_id>/', views.message_history, name='message_history'),
]
