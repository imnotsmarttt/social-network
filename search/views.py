from django.views.generic import ListView
from django.contrib.postgres.search import TrigramWordSimilarity
from django.db.models import Q

from users.models import CustomUser


def is_valid_queryset_param_list(param):
    return param != [] and param is not None


def is_valid_queryset_param_stroke(param):
    return param != '' and param is not None


class SearchUsers(ListView):
    """Search users"""
    model = CustomUser
    template_name = 'search/search.html'
    context_object_name = 'users'

    def get_queryset(self):
        qs = CustomUser.objects.all()
        search_input = self.request.GET.get('search-input')

        if is_valid_queryset_param_stroke(search_input):
            # Search user by first name, last name, username
            qs = qs.annotate(
                similarity_username=TrigramWordSimilarity(search_input, 'username'),
                similarity_first=TrigramWordSimilarity(search_input, 'first_name'),
                similarity_last=TrigramWordSimilarity(search_input, 'last_name'),
            ).filter(
                Q(similarity_username__gt=0.3) |
                Q(similarity_first__gt=0.3) |
                Q(similarity_last__gt=0.3)
            )

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country_filter'] = self.get_queryset().values_list('country', flat=False)
        context['usrs'] = [u for u in self.get_queryset()]
        return context
