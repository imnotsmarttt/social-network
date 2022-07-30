from datetime import timedelta

from django.db import models

from users.models import CustomUser


class Post(models.Model):
    title = models.CharField(max_length=255, verbose_name='Post title')
    body = models.TextField(verbose_name='Post body')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='posts')
    created = models.DateTimeField(auto_now_add=True)
    updated = models.DateTimeField(auto_now=True)
    image = models.ImageField(upload_to='post_img/', blank=True, null=True, verbose_name='Post img')

    class Meta:
        db_table = 'Post'
        ordering = ['-created']

    def __str__(self):
        return self.title

    def updated_at(self):
        # checking a post if it has been changed or not
        return (self.updated - self.created) < timedelta(seconds=1)

    def get_like_users(self):
        return self.likes


class PostLike(models.Model):
    post = models.ForeignKey('Post', on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE, related_name='likes')
