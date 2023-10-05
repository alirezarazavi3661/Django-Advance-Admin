from django.contrib import admin
from .models import Category,Post


class PostAdmin(admin.ModelAdmin):
    """
    Customize admin panel for Posts
    """
    list_display = ['author','title','status','category','created_date','published_date']


"""
registration for Category model in admin panel
"""
admin.site.register(Category)

"""
registration for Post model in admin panel
"""
admin.site.register(Post)
