from django.shortcuts import render
from .models import Post
from .forms import PostForm


def index(request):
    post = Post.objects.all() # получение всех постов

    context = {"title": "Главная страница", "posts": posts}
    return render(request, template_name="blog/index.html", context=context)

def about(request):
    context = {"title": "О сайте"}
    return render(request, template_name="blog/index.html", context=context)

def add_post(request):
    if request.method == "GET":
        post_form = PostForm
        context = {"form": post_form}
        return render(request, template_name="blog/index.html", context=context)

    if request.method == "POST":
        post_