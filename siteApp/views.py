from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Articles

class ArticleList(ListView):
    model = Articles
    template_name = 'article_list.html'
    context_object_name = 'articles'
    ordering = ['-published_at']

class ArticleDetail(DetailView):
    model = Articles
    template_name = 'article_single.html'
    context_object_name = 'article'