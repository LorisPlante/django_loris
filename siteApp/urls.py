from django.urls import path

from .views import ArticleList, ArticleDetail, CategoryList, TagsList

urlpatterns = [
    path('', ArticleList.as_view(), name='article_list'),
    path('article/<int:pk>/', ArticleDetail.as_view(), name='article_detail'),
    path('category/<int:category_id>/', CategoryList, name='cat_list'),
    path('tag/<int:tag_id>/', TagsList, name='tag_list'),
]

