from django.shortcuts import render, reverse
from django.views.generic.edit import CreateView
from django.http import JsonResponse
from django.views.decorators.http import require_POST
from django.contrib.auth.decorators import login_required
from django.contrib.auth.mixins import LoginRequiredMixin

from .forms import CreatePostForm
from .models import PostLike, Post


def index(request):
    return render(request, 'base.html')


class PostCreateView(CreateView, LoginRequiredMixin):
    """Create post view"""
    form_class = CreatePostForm
    template_name = 'posts/create.html'

    def form_valid(self, form):
        # add and save post author
        post = form.save(commit=False)
        post.user = self.request.user
        post.save()
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('index')


@login_required
def post_like(request):
    post_id = request.POST.get('id')
    action = request.POST.get('action')
    print(action)
    if post_id and action:
        try:
            post = Post.objects.get(id=post_id)
            if action == 'like':
                PostLike.objects.create(user=request.user, post=post)
            elif action == 'unlike':
                PostLike.objects.get(post=post, user=request.user).delete()
                return JsonResponse({'status':'ok'})
        except:
            pass
    return JsonResponse({'status':'ok'})