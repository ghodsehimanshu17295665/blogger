from django.shortcuts import render, redirect, HttpResponseRedirect
from blog.forms import PostForm
from django.views.generic import TemplateView
from blog.models import Post
# from django.http import HttpResponse
from .forms import SignUpForm
from django.contrib import messages
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required


class Home(TemplateView):
    template_name = "index.html"

    def get(self, request):
        return render(request, self.template_name)
    

class AllPosts(TemplateView):
    template_name = 'crud/all_posts.html'

    def get(self, request):

        if not request.user.is_authenticated:
            return redirect('/login/')
        
        posts = Post.objects.all()
        context = {
            "posts": posts
        }
        return render(request, self.template_name, context=context)
    

class CreatePost(TemplateView):
    template_name = 'crud/create_post.html'

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
    template_name = 'crud/update_post.html'

    def get(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            form = PostForm(instance=post)
            return render(request, self.template_name, {'form': form})
        # else:
        #     # return HttpResponse("Invalid Post ID....")

    def post(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            form = PostForm(request.POST, instance=post)
            if form.is_valid():
                form.save()
                return render(request, self.template_name, {'form': form})
            else:
                return render(request, self.template_name, {'form': form})
        

class ViewPost(TemplateView):
    template_name = 'crud/view_post.html'

    def get(self, request, pk):
        post = Post.objects.filter(id=pk).first()
        if post:
            return render(request, self.template_name, {"post": post})
        # else:
        #     # return HttpResponse("Post not found.")


class DeletePost(TemplateView):
    template_name = 'crud/all_post.html'

    def post(self, request, pk):
        post = Post.objects.get(id=pk)
        if post:
            post.delete()
            return redirect('allposts')
        return render(request, self.template_name, {'post': post})

# SIGNUP


def sign_up(request):
    if request.user.is_authenticated:
        return redirect('/')
    if request.method == "POST":
        form = SignUpForm(request.POST)
        if form.is_valid():
            messages.success(request, "Account Created Successfully!!")
            form.save()
    else:
        form = SignUpForm()
    return render(request, 'enroll/signup.html', {'form': form})
    
# Login


def user_login(request):
    if not request.user.is_authenticated:
        if request.method == "POST":
            form = AuthenticationForm(request=request, data=request.POST)
            if form.is_valid():
                user_name = form.cleaned_data['username']
                user_pass = form.cleaned_data['password']
                user = authenticate(username=user_name, password=user_pass)
                if user is not None:
                    login(request, user)
                    messages.success(request, 'Logged in Successfully')
                    return redirect('/profile/')
                else:
                    form.add_error(None, 'Invalid username or password')
        else:
            form = AuthenticationForm()
        return render(request, 'enroll/userlogin.html', {'form': form})
    else:
        return HttpResponseRedirect('/profile/')


# profile


def user_profile(request):
    if request.user.is_authenticated:
        return render(request, 'enroll/profile.html', {'name': request.user})
    else:
        return HttpResponseRedirect('/login/')

# logout


def user_logout(request):
    logout(request)
    return HttpResponseRedirect('/login/')


 

