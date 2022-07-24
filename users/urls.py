from django.urls import path, reverse_lazy
from django.contrib.auth.views import LoginView, LogoutView

from . import views
from .forms import UserLoginForm

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='users/login.html', form_class=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout')
]