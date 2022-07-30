from django.urls import path
from django.contrib.auth.views import LoginView, LogoutView
from django.contrib.staticfiles.urls import static, settings

from . import views
from .forms import UserLoginForm

urlpatterns = [
    path('login/', LoginView.as_view(
        template_name='users/login.html', form_class=UserLoginForm), name='login'),
    path('logout/', LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),

    path('<slug:slug>/', views.UserProfileView.as_view(), name='profile'),
    path('<slug:slug>/change/', views.UserProfileUpdate.as_view(), name='profile_update'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)