from django.db import models
from mptt.models import MPTTModel, TreeForeignKey

from posts.models import Post
from users.models import CustomUser


class CommentModel(MPTTModel):
    """Comment mptt model"""
    user = models.ForeignKey(CustomUser, on_delete=models.CASCADE)
    post = models.ForeignKey(Post, on_delete=models.CASCADE, related_name='comments')
    parent = TreeForeignKey('self', on_delete=models.CASCADE, related_name='child', null=True)
    content = models.TextField(verbose_name='Comment body')
    created = models.DateTimeField(auto_now_add=True)

    class Meta:
        db_table = 'Comments'

    class MPTTMeta:
        order_insertion_by = '-created'
