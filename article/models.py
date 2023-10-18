from django.db import models

# Create your models here.
class ArticleContentTab(models.Model):
    author = models.CharField(max_length=100)
    email = models.EmailField()
    organization = models.CharField(max_length=100)
    title = models.CharField(max_length=100)
    content = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

