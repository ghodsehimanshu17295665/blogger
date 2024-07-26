from django.urls import path
from blog.views import home
from django.conf import settings
from django.conf.urls.static import static


urlpatterns = [
    path("", home),
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)