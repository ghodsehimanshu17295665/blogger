from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import read_post
from .views import (home, create_post, post_list,
                    delete_post, update_post)

urlpatterns = [
    path("", home),
    path('post/list/', post_list, name='post_list'),
    path('create/post/', create_post, name='create_post'),
    path('delete/post/<uuid:pk>/', delete_post, name='delete_post'),
    path('update/post/<uuid:pk>/', update_post, name='update_post'),
    path('view/post/<uuid:pk>/', read_post, name='read_post'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
