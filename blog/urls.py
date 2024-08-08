from django.urls import path
from django.conf.urls.static import static
from django.conf import settings
from .views import Home, PostList, CreatePost, UpdatePost, ViewPost, DeletePost

urlpatterns = [
    path('', Home.as_view(), name='home'),
    path('post/list/', PostList.as_view(), name='post_list'),
    path('create/post/', CreatePost.as_view(), name='create_post'),
    path('post/update/<uuid:pk>/', UpdatePost.as_view(), name='post_update'),
    path('post/view/<uuid:pk>/', ViewPost.as_view(), name='view_post'),
    path('post/delete/<uuid:pk>/', DeletePost.as_view(), name='delete_post'),

]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
