from django.contrib import admin

from .models import Institution, Researcher, Article, Post, ShortPost

# Register your models here.

admin.site.register(Institution)
admin.site.register(Researcher)
admin.site.register(Article)
admin.site.register(Post)
admin.site.register(ShortPost)

