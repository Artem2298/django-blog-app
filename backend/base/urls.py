from django.urls import path
from . import views
from .apiviews import ArticleList


urlpatterns = [
    path('', views.home, name='home'),
    path('article', views.article, name='article'),
    path('api/articles/', ArticleList.as_view(), name='article-list'),
]