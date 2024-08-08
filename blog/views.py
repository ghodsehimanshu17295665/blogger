from django.shortcuts import render, redirect
from django.http import HttpResponse
from blog.forms import PostForm
from django.views.generic import TemplateView
from blog.models import Post
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class Home(TemplateView):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)


class PostList(TemplateView):
    template_name = 'blog/list_post.html'

    def get(self, request):
        if not request.user.is_authenticated:
            return redirect('/login/')

        posts = Post.objects.all()
        context = {
            "posts": posts
        }
        return render(request, self.template_name, context=context)


class CreatePost(TemplateView):
    template_name = 'blog/create_post.html'

    def get(self, request):
        form = PostForm()
        return render(request, self.template_name, {'form': form})

    def post(self, request):
        form = PostForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("create_post")
        else:
            form = PostForm()
        return render(request, self.template_name, {"form": form})


class UpdatePost(TemplateView):
    template_name = 'blog/update_post.html'

    def get(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            form = PostForm(instance=post)
            return render(request, self.template_name, {'form': form})
        else:
            return HttpResponse("Invalid Post ID....")

    def post(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return render(request, self.template_name, {'form': form})
            else:
                return render(request, self.template_name, {'form': form})
        else:
            return HttpResponse("Invalid Post ID....")


class ViewPost(TemplateView):
    template_name = 'blog/read_post.html'

    def get(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            return render(request, self.template_name, {"post": post})
        else:
            return HttpResponse("Post not found.")


class DeletePost(TemplateView):
    template_name = 'blog/list_post.html'

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        if post:
            post.delete()
            return redirect('post_list')
        return render(request, self.template_name, {'post': post})


# SignUp View Function
def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == 'POST':
        form = SignUpForm(request.POST)
        if form.is_valid():
            form.save()
            messages.success(request, "Account Created Successfully!!")
            return redirect('login')
    else:
        form = SignUpForm()
    return render(request, 'registration/signup.html', {'form': form})


# Login View Function
def user_login(request):
    if not request.user.is_authenticated:
        if request.method == 'POST':
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_password = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_password)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully!!')
                    return redirect('/profile/')
                else:
                    form.add_error(None, 'Invalid username or password')
        else:
            form = AuthenticationForm()
        return render(request, 'registration/userlogin.html', {'form': form})
    else:
        return redirect('/profile/')


# Profile
def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'registration/profile.html')
    else:
        return redirect('/login/')


# Logout
def user_logout(request):
    logout(request)
    return redirect('/login/')
