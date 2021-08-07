from django.shortcuts import render, get_object_or_404
from .models import Post, Group


def group_posts(request, slug):
    template = 'posts/group_list.html'
    group = get_object_or_404(Group, slug=slug)
    posts = group.posts.all()
    context = {
        'group': group,
        'posts': posts,
    }
    return render(request, template, context)


def index(request):
    template = 'posts/index.html'
    posts = Post.objects

    context = {
        'posts': posts
    }
    return render(request, template, context)
