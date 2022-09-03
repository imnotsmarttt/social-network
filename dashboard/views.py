from django.views.generic import ListView
from django.views.generic.edit import FormMixin
from django.contrib.auth.mixins import LoginRequiredMixin

from posts.models import Post
from comments.forms import CommentCreateForm


class DashboardFeed(LoginRequiredMixin, ListView, FormMixin):
    model = Post
    template_name = 'dashboard/feed.html'
    form_class = CommentCreateForm
    context_object_name = 'posts'
    
    def get_queryset(self):
        follow_to = self.request.user.contact_from.all().values_list('user_to', flat=True)
        return Post.objects.filter(user_id__in=follow_to)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Checking which posts the user has liked
            context['user_likes'] = self.request.user.likes.all().values_list('post', flat=True)
        return context