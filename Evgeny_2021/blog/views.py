from .models import Category, Post, Comment
from django.shortcuts import render


def blog_index(request):
    orderby = Post.created_on()
    context = {
        'orderby': orderby
    }
    return render(request, 'blog_index.html', context)


def blog_detail(request, pk):
    text = Post.body.get(pk=pk)
    context = {
        'text': text
    }
    return render(request, 'blog_detail.html', context)



