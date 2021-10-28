from django.contrib import admin
from .models import Post,Comment,SavePost
# Register your models here.

admin.site.register(Post)

admin.site.register(Comment)

admin.site.register(SavePost)

