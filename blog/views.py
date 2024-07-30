from django.shortcuts import render
# from django.http import HttpResponse
from .models import Post


# Create your views here.
def home(request):
    return render(request, "index.html")


def post_list(request):
    posts = Post.objects.all()
    return render(request, 'post_list.html', {'posts': posts})
