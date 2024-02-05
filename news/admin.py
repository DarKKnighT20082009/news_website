from django.contrib import admin

from news.models import News, NewsCategory, NewsImage, Comment

# Register your models here.
admin.site.register(News)
admin.site.register(NewsImage)
admin.site.register(NewsCategory)
admin.site.register(Comment)