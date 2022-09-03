from django.urls import path

from . import views

urlpatterns = [
    path('post/', views.comment_create, name='comment_post')
]