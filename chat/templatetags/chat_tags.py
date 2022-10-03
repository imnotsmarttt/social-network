from django import template

from chat.models import Message

register = template.Library()


@register.simple_tag
def get_compation(user, chat):
    for u in chat.members.all():
        if u != user:
            return u
    return None


@register.simple_tag
def check_unread_messages(chat_id, user):
    return Message.objects.filter(chat=chat_id, is_read=False, author=user).count()
