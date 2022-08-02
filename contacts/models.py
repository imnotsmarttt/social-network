from django.db import models

from users.models import CustomUser


class Contact(models.Model):
    """User contact model"""
    user_from = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contact_from')
    user_to = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='contact_to')
    created = models.DateTimeField(auto_now_add=True)
    
    class Meta:
        ordering = ('-created', )
        db_table = 'Contact'
