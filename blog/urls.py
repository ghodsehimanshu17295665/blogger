from django.urls import path
from blog.views import home
from django.conf import settings
from django.conf.urls.static import static
from .views import all_posts, create_post, update_post, view_post, delete_post


urlpatterns = [
    path("", home),
    path('all/posts/', all_posts, name='all_posts'),
    path('create/post/', create_post, name='create_post'),
    path('update/post/<uuid:pk>/', update_post, name='update_post'),
    path('view/post/<uuid:pk>/', view_post, name='view_post'),
    path('delete/post/<uuid:pk>/', delete_post, name='delete_post'),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)



