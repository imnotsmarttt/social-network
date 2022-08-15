from django import template

register = template.Library()


@register.simple_tag
def get_compation(user, chat):
    for u in chat.members.all():
        if u != user:
            return u
    return None
