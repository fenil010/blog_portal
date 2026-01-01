from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Post
from .forms import PostForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login
from .models import Post

@login_required
def my_vlog(request):
    # Fetch only blogs created by logged-in user
    posts = Post.objects.filter(author=request.user).order_by('-created_at')
    return render(request, 'blog/my_vlog.html', {'posts': posts})




def home(request):
    posts = Post.objects.all().order_by('-created_at')
    return render(request, 'blog/home.html', {'posts': posts})


def post_detail(request, id):
    post = get_object_or_404(Post, id=id)
    return render(request, 'blog/post_detail.html', {'post': post})


@login_required
def post_create(request):
    if request.method == 'POST':
        form = PostForm(request.POST)
        if form.is_valid():
            post = form.save(commit=False)
            post.author = request.user
            post.save()
            messages.success(request, "Blog created successfully!")
            return redirect('home')
    else:
        form = PostForm()

    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_update(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return redirect('home')

    form = PostForm(request.POST or None, instance=post)
    if form.is_valid():
        form.save()
        messages.success(request, "Blog updated successfully!")
        return redirect('post_detail', id=post.id)

    return render(request, 'blog/post_form.html', {'form': form})


@login_required
def post_delete(request, id):
    post = get_object_or_404(Post, id=id)

    if post.author != request.user:
        return redirect('home')

    if request.method == 'POST':
        post.delete()
        messages.success(request, "Blog deleted successfully!")
        return redirect('home')

    return render(request, 'blog/post_confirm_delete.html', {'post': post})

def signup(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)  # auto login after signup
            return redirect('home')
    else:
        form = UserCreationForm()

    return render(request, 'auth/signup.html', {'form': form})

