# from django.contrib import admin
from django.urls import path
from .views import home
from .views import post_list
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path("", home),
    path('post_list/', post_list, name='post_list'),
]+static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
