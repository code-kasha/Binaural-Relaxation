from django.contrib import messages
from apps.blog.forms import PostForm
from django.shortcuts import redirect, render

from .models import Post, Comment


def blog_home(request):
    posts = Post.objects.all()
    context = {"posts": posts}
    return render(request, "blog/blog_home.html", context)


def create_post(request):
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            instance = form.save(commit=False)
            instance.user = request.user
            instance.save()
            messages.success(request, "Post Created!")
            return redirect("blog:home")
    else:
        form = PostForm()
    return render(request, "blog/create_post.html", {"form": form})


def post_details(request, pk):
    post = Post.objects.get(id=pk)
    context = {"post": post}
    return render(request, "blog/post_details.html", context)


def update_post(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        form = PostForm(request.POST)
        if form.is_valid():
            post.title = form.cleaned_data.get("title")
            post.content = form.cleaned_data.get("content")
            post.save()
        messages.success(request, "Post Updated!")
        return redirect("blog:post_details", pk=pk)
    else:
        form = PostForm(instance=post)
    return render(request, "blog/update_post.html", {"form": form})


def delete_post(request, pk):
    obj = Post.objects.get(pk=pk)
    if request.method == "POST":
        title = obj.title
        obj.delete()
        messages.success(request, f"{title} deleted succesfully")
        return redirect("blog:home")
    context = {"obj": obj}
    return render(request, "blog/delete_post.html", context)


def toggle_like(request, pk):
    obj = Post.objects.get(pk=pk)
    if request.method == "POST":
        if request.user in obj.likes.all():
            obj.likes.remove(request.user)
        else:
            obj.likes.add(request.user)

        return redirect("blog:home")
    return redirect("blog:post_details", pk=pk)


def comment(request, pk):
    post = Post.objects.get(pk=pk)
    if request.method == "POST":
        content = request.POST.get("content")

        obj = Comment.objects.create(user=request.user, title=content)
        post.comments.add(obj)
        messages.success(request, "comment added!")

        return redirect("blog:post_details", pk=pk)
    return redirect("blog:home")
