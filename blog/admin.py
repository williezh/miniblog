from django.contrib import admin
from blog.models import Article, Category, Tag
#from .user_admin import UserAdmin,MyProfile

#admin.site.register(MyProfile, UserAdmin)  
admin.site.register(Article)
admin.site.register(Category)
admin.site.register(Tag)
