from django.contrib import admin
from .models import Post


class PostAdmin(admin.ModelAdmin):
   list_display = ('author', 'age', 'title', 'comment', 'date_posted')
   
admin.site.register(Post, PostAdmin)