from django.db import models

from users.models import CustomUser


class Chat(models.Model):
    members = models.ManyToManyField(CustomUser, related_name='chats')


class Message(models.Model):
    chat = models.ForeignKey('Chat', on_delete=models.CASCADE, related_name='messages')
    author = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='sent_messages')
    created = models.DateTimeField(auto_now_add=True)
    content = models.TextField()
    is_readed = models.BooleanField(default=False)
