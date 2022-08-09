from django.urls import path
from django.contrib.auth import views as auth_views
from django.contrib.staticfiles.urls import static, settings

from . import views
from .forms import UserLoginForm, CustomPasswordChangeForm

urlpatterns = [
    path('login/', auth_views.LoginView.as_view(
        template_name='users/login.html', form_class=UserLoginForm), name='login'
         ),
    path('logout/', auth_views.LogoutView.as_view(template_name='users/logout.html'), name='logout'),
    path('register/', views.UserRegisterView.as_view(), name='register'),
    path('password_change/', auth_views.PasswordChangeView.as_view(
        template_name='users/password_change.html', form_class=CustomPasswordChangeForm), name='password_change'
         ),
    path('password_change/done/', auth_views.PasswordChangeDoneView.as_view(), name='password_change_done'),

    path('<slug:slug>/', views.UserProfileView.as_view(), name='profile'),
    path('<slug:slug>/update/', views.UserProfileUpdate.as_view(), name='profile_update'),

]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
