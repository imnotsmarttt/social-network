from django.db.models import Q
from django.views.generic import ListView
from django.contrib.postgres.search import TrigramWordSimilarity
from users.models import CustomUser


def is_valid_queryset_param_list(param):
    return param != [] and param is not None


def is_valid_queryset_param_stroke(param):
    return param != '' and param is not None


class SearchUsers(ListView):
    model = CustomUser
    template_name = 'search/search.html'
    context_object_name = 'users'

    def get_queryset(self):
        qs = CustomUser.objects.all()
        search_input = self.request.GET.get('search-input')

        if is_valid_queryset_param_stroke(search_input):
            qs = qs.annotate(similarity=TrigramWordSimilarity(search_input, 'username'),).filter(similarity__gt=0.3)

        return qs

    def get_context_data(self, *, object_list=None, **kwargs):
        context = super().get_context_data(**kwargs)
        context['country_filter'] = self.get_queryset().values_list('country', flat=False)
        context['usrs'] = [u for u in self.get_queryset()]
        return context
