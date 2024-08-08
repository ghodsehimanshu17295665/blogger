from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, AllPosts, CreatePost, UpdatePost, ViewPost, DeletePost

urlpatterns = [

      path('', Home.as_view(), name='home'),
      path('all/posts/', AllPosts.as_view(), name='allposts'),
      path('create/post/', CreatePost.as_view(), name='create_post'),
      path('update/post/<uuid:pk>', UpdatePost.as_view(), name='update_post'),
      path('view/post/<uuid:pk>', ViewPost.as_view(), name='view_post'),
      path('delete/post/<uuid:pk>', DeletePost.as_view(), name='delete_post'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)





