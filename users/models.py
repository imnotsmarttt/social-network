from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Extended user model"""
    birthday = models.DateField(verbose_name='Day of birth', null=True)
    avatar = models.ImageField(upload_to='user_avatar/', verbose_name='User image', null=True, blank=True)
    about_me = models.TextField(verbose_name='About User', null=True, blank=True)
    city = models.CharField(max_length=255, verbose_name='City', null=True)
    country = models.CharField(max_length=255, verbose_name='Country', null=True)

    class Meta:
        db_table = 'CustomUser'
