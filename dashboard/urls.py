from django.urls import path


from . import views

app_name = 'dashboard'


urlpatterns = [
    path('feed/', views.DashboardFeed.as_view(), name='feed'),
]