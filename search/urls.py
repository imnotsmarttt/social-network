from django.urls import path

from . import views


urlpatterns = [
    path('', views.SearchUsers.as_view(), name='search')
]
