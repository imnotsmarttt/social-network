from django.shortcuts import redirect, reverse
from django.views.generic.edit import CreateView
from django.views.generic import DetailView, UpdateView
from django.contrib.auth import login, authenticate


from .forms import UserRegisterForm, UserUpdateCustomForm
from .models import CustomUser


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


class UserProfileView(DetailView):
    model = CustomUser
    template_name = 'users/profile.html'
    context_object_name = 'user'


class UserProfileUpdate(UpdateView):
    template_name = 'users/update_profile.html'
    form_class = UserUpdateCustomForm
    model = CustomUser


    def get_success_url(self):
        return reverse('profile', kwargs={'slug': self.request.user.slug})
