from django.shortcuts import render, redirect
from django.http import HttpResponse
from .models import Post
from blog.forms import PostForm
from django.contrib import messages


def home(request):
    return render(request, "index.html")


def post_list(request):
    posts = Post.objects.all()
    # breakpoint()
    return render(request, "blog/list_post.html", {"posts": posts})


def create_post(request):
    """
    This Function will Add New Item and Show All Items
    """
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, "Your Post has been created!!!")
            return redirect("create_post")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})


def delete_post(request, pk):
    """
    This Function will Delete Post if available
    """
    post = Post.objects.filter(id=pk)
    if request.method == "POST":
        post.delete()
        messages.info(request, "Post Deleted Successfully")
        return redirect("/post/list/")
    return render(request, "blog/list_post.html", {"post": post})


def update_post(request, pk):
    """
    This function will be Update Post if available
    """
    post = Post.objects.filter(id=pk).first()
    if request.method == "POST":
        if post:
            data = request.POST
            form = PostForm(data, instance=post)
            if form.is_valid():
                form.save()
                messages.info(request, "Post Updated Successfully")
        else:
            return HttpResponse("Invalid Post ID....")
    else:
        form = PostForm(instance=post)
    return render(request, "blog/update_post.html", {"form": form})


def read_post(request, pk):
    """
    This function will be View Post if available
    """
    post = Post.objects.filter(id=pk).first()
    return render(request, "blog/read_post.html", {"post": post})
