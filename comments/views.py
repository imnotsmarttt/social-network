from django.contrib.auth.decorators import login_required
from django.http import JsonResponse

from .models import CommentModel
from .forms import CommentCreateForm

from posts.models import Post


@login_required
def comment_create(request):
    if request.headers.get('x-requested-with') == 'XMLHttpRequest':
        try:
            reply_id = int(request.POST.get('parent_id'))
        except:
            reply_id = None
        parent = None
        user = request.user
        post = Post.objects.get(id=request.POST.get('post_id'))
        content = request.POST['content']
        if reply_id:
            parent = CommentModel.objects.get(id=reply_id)

        CommentModel.objects.create(user=user, post=post, parent=parent, content=content)
        node = CommentModel.objects.order_by('id').last().id
        return JsonResponse({'status': 'ok', 'node': node, 'post': post.id})
    return JsonResponse({'status': 'false'})

