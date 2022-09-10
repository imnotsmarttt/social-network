from django.shortcuts import reverse
from django.http import HttpResponseRedirect
from django.views.generic.edit import CreateView, FormMixin
from django.views.generic import DetailView, UpdateView
from django.contrib.auth import login, authenticate
from django.contrib.auth.mixins import LoginRequiredMixin


from .forms import UserRegisterForm, UserUpdateCustomForm
from .models import CustomUser

from comments.forms import CommentCreateForm


class UserRegisterView(CreateView):
    template_name = 'users/register.html'
    form_class = UserRegisterForm

    def form_valid(self, form):
        form.save()
        username = form.cleaned_data.get('username')
        password = form.cleaned_data.get('password1')
        user = authenticate(username=username, password=password)
        login(self.request, user)
        return HttpResponseRedirect(reverse('profile', kwargs={'slug': user.slug}))


class UserProfileView(DetailView, FormMixin):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'user'
    form_class = CommentCreateForm


class UserProfileUpdate(LoginRequiredMixin, UpdateView):
    template_name = 'users/update_profile.html'
    form_class = UserUpdateCustomForm
    model = CustomUser

    def get_success_url(self):
        return reverse('profile', kwargs={'slug': self.request.user.slug})
