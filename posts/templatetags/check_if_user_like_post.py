from django import template

register = template.Library()


@register.simple_tag
def check_if_user_like_post(user, post):
    if post.id in user.likes.all().values_list('post', flat=True):
        return True
    return False


