from django.contrib import admin

from blog.models import Post
from .models import User,Comment,Followers

admin.site.register(Post)
admin.site.register(User)
admin.site.register(Comment)
admin.site.register(Followers)
