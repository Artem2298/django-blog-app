from django.db import models

class User(models.Model):
    user_id = models.AutoField(primary_key=True)
    first_name = models.CharField(max_length=50, null=False)
    last_name = models.CharField(max_length=50, null=False)
    username = models.CharField(max_length=50, unique=True, null=False)
    phone_number = models.CharField(max_length=16, null=True, blank=True)
    email = models.EmailField(unique=True, null=False)
    password = models.CharField(max_length=255, null=False)
    created_time = models.DateTimeField(auto_now_add=True)
    deleted_time = models.DateTimeField(null=True, blank=True)
    
    class Meta:
        constraints = [
            models.CheckConstraint(check=models.Q(phone_number__regex=r'^\+?\d{10,16}$'), name='valid_phone_number')
        ]

    
    def __str__(self):
        return f"{self.username}"
    
class Article(models.Model):
    article_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=255, null=False)
    content = models.TextField(null=False)
    user_id = models.ForeignKey(User, on_delete=models.CASCADE, related_name='articles')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(null=True, blank=True)
    deleted_time = models.DateTimeField(null=True, blank=True)

    def __str__(self):
        return f"{self.title}"

class Category(models.Model):
    category_id = models.AutoField(primary_key=True)
    name = models.CharField(max_length=100, unique=True, null=False)
    description = models.TextField(null=False)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['name'], name='unique_category_name')
        ]

    def __str__(self):
        return self.name

class ArticleCategory(models.Model):
    article = models.ForeignKey(Article, on_delete=models.CASCADE)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['article', 'category'], name='unique_article_category')
        ]

    def __str__(self):
        return f"{self.article} - {self.category}"
    
class Comment(models.Model):
    comment_id = models.AutoField(primary_key=True)
    content = models.TextField(null=False)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='comments')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='comments')
    created_time = models.DateTimeField(auto_now_add=True)
    updated_time = models.DateTimeField(null=True, blank=True)

    class Meta:
        constraints = [
            models.CheckConstraint(check=~models.Q(content=''), name='comment_not_empty'),
            models.CheckConstraint(check=~models.Q(content__isnull=True), name='comment_not_null')
        ]

    def __str__(self):
        return f"{self.user} - {self.article}"

class Like(models.Model):
    like_id = models.AutoField(primary_key=True)
    article = models.ForeignKey(Article, on_delete=models.CASCADE, related_name='likes')
    user = models.ForeignKey(User, on_delete=models.CASCADE, related_name='likes')
    created_time = models.DateTimeField(auto_now_add=True)

    class Meta:
        constraints = [
            models.UniqueConstraint(fields=['article', 'user'], name='unique_article_user')
        ]
        
    def __str__(self):
        return f"{self.article.title} - {self.user.username}"
    