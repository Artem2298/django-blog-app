from django.contrib import admin
from .models import User, Article, Comment, Like, Category, ArticleCategory

admin.site.register(User)
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Comment)
admin.site.register(Like)
admin.site.register(ArticleCategory)