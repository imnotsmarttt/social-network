from django.shortcuts import reverse
from django.views.generic.edit import CreateView
from django.http import JsonResponse

from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreatePostForm
from .models import PostLike, Post


class PostCreateView(CreateView, LoginRequiredMixin):
    """Create post view"""
    form_class = CreatePostForm
    model = Post
    template_name = 'posts/create.html'

    def form_valid(self, form):
        # add and save post author
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('profile', kwargs={'slug': self.request.user})


@login_required
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    if post_id and action:
        post = Post.objects.get(id=post_id)
        if action == 'like':
            PostLike.objects.get_or_create(user=request.user, post=post)
        elif action == 'unlike':
            PostLike.objects.get(post=post, user=request.user).delete()
    return JsonResponse({'status': 'ok'})