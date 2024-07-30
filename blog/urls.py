from django.urls import path
from blog.views import home
from django.conf import settings
from django.conf.urls.static import static
from .views import post_list


urlpatterns = [
    path("", home),
    path('post_list/', post_list, name='post_list') 

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
