from django.contrib import admin
from django.contrib.auth.models import User, Group
from .models import Post, Comment, Category
# Register your models here.
admin.site.register(Post)
admin.site.register(Comment)
admin.site.register(Category)
admin.site.unregister(User)
admin.site.unregister(Group)