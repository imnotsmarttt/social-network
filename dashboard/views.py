from django.views.generic import ListView
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post


class DashboardFeed(LoginRequiredMixin, ListView):
    model = Post
    template_name = 'dashboard/feed.html'
    context_object_name = 'posts'
    
    def get_queryset(self):
        follow_to = self.request.user.contact_from.all().values_list('user_to', flat=True)
        return Post.objects.filter(user_id__in=follow_to)
