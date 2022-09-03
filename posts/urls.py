from django.urls import path
from django.contrib.staticfiles.urls import static, settings

from . import views

urlpatterns = [
    path('create/', views.PostCreateView.as_view(), name='post_create'),
    path('like/', views.post_like, name='post_like'),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
