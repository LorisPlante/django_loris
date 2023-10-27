from django.urls import path

from .views import ArticleList, ArticleDetail

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
]

