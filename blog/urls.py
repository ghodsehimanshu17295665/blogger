from django.urls import path
from django.conf import settings
from django.conf.urls.static import static
from .views import Home, AllPosts, CreatePost, UpdatePost, ViewPost, DeletePost
from django.contrib.auth.views import LoginView
 

urlpatterns = [

      path('', Home.as_view(), name='home'),
      path('all/posts/', AllPosts.as_view(), name='allposts'),
      path('create/post/', CreatePost.as_view(), name='create_post'),
      path('update/post/<uuid:pk>', UpdatePost.as_view(), name='update_post'),
      path('view/post/<uuid:pk>', ViewPost.as_view(), name='view_post'),
      path('delete/post/<uuid:pk>', DeletePost.as_view(), name='delete_post'),
      # path("", user_views.homePage, name="home-page"),
      # path("login-user/", LoginView.as_view(template_name="user/loginView.html"),
      #    name="login-user"),
      # path("student-view/", user_views.studentView, name="student-view"),
      # path("teacher-view/", user_views.teacherView, name="teacher-view"),
      # path("principal-view/", user_views.principalView, name="principal-view"),

]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

if settings.DEBUG:  
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


