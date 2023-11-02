from django.shortcuts import render

from django.views.generic import ListView, DetailView
from .models import Articles, Categories, Tags

class ArticleList(ListView):
    model = Articles
    template_name = 'article_list.html'
    context_object_name = 'articles'
    ordering = ['-published_at', 'title']

class ArticleDetail(DetailView):
    model = Articles
    template_name = 'article_single.html'
    context_object_name = 'article'

def CategoryList(request, category_id):
    # aller chercher la categorie en question
    currentCategory = Categories.objects.get(pk=category_id)

    # aller chercher les articles de la categorie
    articles = Articles.objects.filter(category=currentCategory) # premiere varieble est celle du model

    # définir un "context" (les infos à afficher)
    context= {
        'title' : currentCategory.title,
        'articles' : articles,
    }

    # effectuer le "rendu"
    return render(request, 'filters.html', context)

def TagsList(request, tag_id):
    # aller chercher le tag en question
    currentTags = Tags.objects.get(pk=tag_id)

    # aller chercher les articles du tag
    articles = Articles.objects.filter(tags=currentTags) # premiere varieble est celle du model

    # définir un "context" (les infos à afficher)
    context= {
        'title' : currentTags.word,
        'articles' : articles,
    }

    # effectuer le "rendu"
    return render(request, 'filters.html', context)