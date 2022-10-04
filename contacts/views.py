from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import Contact
from users.models import CustomUser


@require_POST
@login_required
def add_contact(request):
    action = request.POST.get('action')
    user_to = request.POST.get('id')
    if action and user_to:
        user = CustomUser.objects.get(id=user_to)
        if action == 'follow':
            Contact.objects.get_or_create(user_from=request.user, user_to=user)
        else:
            Contact.objects.filter(user_from=request.user, user_to=user).delete()

    return JsonResponse({'status':'ok'})
