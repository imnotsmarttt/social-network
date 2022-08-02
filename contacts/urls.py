from django.urls import path

from . import views


urlpatterns = [
    path('follow/', views.add_contact, name='follow_to_user'),
]