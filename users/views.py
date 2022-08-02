from django.shortcuts import redirect, reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, FormMixin
from django.views.generic import DetailView, UpdateView
from django.contrib.auth import login, authenticate


from .forms import UserRegisterForm, UserUpdateCustomForm
from .models import CustomUser

from comments.forms import CommentCreateForm
from comments.models import CommentModel
from posts.models import Post


class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return redirect('index')


class UserProfileView(DetailView, FormMixin):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'user'
    form_class = CommentCreateForm

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        if self.request.user.is_authenticated:
            # Checking which posts the user has liked
            context['user_likes'] = self.request.user.likes.all().values_list('post', flat=True)
        # Checking user_followers
        context['user_followers'] = self.get_object().contact_to.all().values_list('user_from', flat=True)
        return context

    def post(self, request, *args, **kwargs):
        self.object = self.get_object()
        form = self.get_form()
        if form.is_valid():
            return self.form_valid(form)
        else:
            return self.form_invalid(form)

    def form_valid(self, form):
        try:
            reply_id = int(self.request.POST.get('parent_id'))
        except:
            reply_id = None
        comment = form.save(commit=False)
        comment.user = self.request.user
        comment.post = Post.objects.get(id=self.request.POST['post_id'])
        if reply_id:
            comment.parent = CommentModel.objects.get(id=reply_id)
        comment.save()
        return HttpResponseRedirect(reverse('profile', kwargs={'slug': comment.user.slug}))


class UserProfileUpdate(UpdateView):
    template_name = 'users/update_profile.html'
    form_class = UserUpdateCustomForm
    model = CustomUser

    def get_success_url(self):
        return reverse('profile', kwargs={'slug': self.request.user.slug})
