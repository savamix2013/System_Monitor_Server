from django.urls import path
from . import views

app_name = 'system_monitor_servers'

urlpatterns = [
    path('', views.index, name='index'),  # Створює маршрут для 'index'
    path('servers/', views.servers, name='servers'),
    path('topics/', views.topics, name='topics'),  # Створює маршрут для 'topics'
    path('servers/<int:server_id>/', views.server, name='server'),
    path('new_server/', views.new_server, name='new_server'),
]
