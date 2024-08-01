from django.shortcuts import render, redirect
from .models import Post
from blog.forms import PostForm
from django.contrib import messages


def home(request):
    return render(request, "index.html")


def all_posts(request):
    posts = Post.objects.all()
    return render(request, 'crud/all_posts.html', {'posts': posts})


def create_post(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            messages.info(request, 'Post Created Successfully!!')
    else:
        form = PostForm()

    return render(request, 'crud/create_post.html', {'form': form})


def update_post(request, pk):
    post = Post.objects.filter(id=pk).first()
    if request.method == 'POST':
        if post:
            data = request.POST
            form = PostForm(data, instance=post)
            if form.is_valid():
                form.save()
        else:
            return messages.info(request, 'Invalid Post ID!!')

    else:
        form = PostForm(instance=post)

    return render(request, 'crud/update_post.html', {'form': form})


def view_post(request, pk):
    post = Post.objects.filter(id=pk).first()
    return render(request, 'crud/view_post.html', {'post': post})


def delete_post(request, pk):
    post = Post.objects.filter(id=pk)
    if request.method == 'POST':
        post.delete()
        messages.info(request, 'Post Deleted Successfully!!')
        return redirect('/all/posts/')
    return render(request, 'crud/all_posts.html', {'post': post})
