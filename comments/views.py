from django.shortcuts import reverse
from django.http import HttpResponseRedirect

from .models import CommentModel
from .forms import CommentCreateForm

from posts.models import Post


def comment_create(request):
    if request.method == 'POST':
        form = CommentCreateForm(request.POST)
        try:
            reply_id = int(request.POST.get('parent_id'))
        except:
            reply_id = None
        comment = form.save(commit=False)
        comment.user = request.user
        comment.post = Post.objects.get(id=request.POST['post_id'])
        if reply_id:
            comment.parent = CommentModel.objects.get(id=reply_id)
        comment.save()
        return HttpResponseRedirect(reverse('profile', kwargs={'slug': comment.user.slug}))