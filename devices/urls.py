from django.urls import path
from . import views

urlpatterns = [
    path('', views.device_list, name='device_list'),
    path('create/', views.device_create, name='device_create'),
    path('<int:device_id>/', views.device_detail, name='device_detail'),
    path('<int:device_id>/delete/', views.device_delete, name='device_delete'),
    path('api/status/', views.device_status_api, name='device_status_api'),
]
