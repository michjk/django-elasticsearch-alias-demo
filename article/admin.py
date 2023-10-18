from django.contrib import admin
from .models import ArticleContentTab
# Register your models here.

@admin.register(ArticleContentTab)
class ArticleContentTabAdmin(admin.ModelAdmin):
    list_display = ["id", "title", "author"]
    search_fields = ["title", "author"]