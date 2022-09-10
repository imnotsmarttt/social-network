from django import template

register = template.Library()


@register.simple_tag
def check_contact(user1, user2):
    if user1.id in user2.contact_to.all().values_list('user_from', flat=True):
        return True
    return False


