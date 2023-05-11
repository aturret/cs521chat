from django.urls import path
from . import views

app_name = 'cs521chat'

urlpatterns = [
path('', views.chat_view, name='chat_view'),
path('post_message/', views.post_message, name='post_message'),
]