from django.db import models
from django.contrib.auth.models import AbstractUser


class CustomUser(AbstractUser):
    """Extended user model"""
    slug = models.SlugField(db_index=True, unique=True, null=True)
    avatar = models.ImageField(upload_to='user_avatar/', verbose_name='User image', null=True, blank=True)
    about_me = models.TextField(verbose_name='About User', null=True, blank=True)
    city = models.CharField(max_length=255, verbose_name='City', null=True)
    country = models.CharField(max_length=255, verbose_name='Country', null=True)
    phone = models.CharField(max_length=25, blank=True, null=True, verbose_name='Phone number')

    class Meta:
        db_table = 'CustomUser'

    def save(self, *args, **kwargs):
        self.slug = self.username
        return super(CustomUser, self).save(*args, **kwargs)
