from django.urls import path

from . import views

urlpatterns = [
    path('list/', views.ChatList.as_view(), name='chat_list'),
    path('create/<int:user_id>/', views.ChatCreate.as_view(), name='chat_create'),
    path('<int:chat_id>/', views.MessagesView.as_view(), name='chat_messages'),
]
