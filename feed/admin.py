from django.contrib import admin

# Register your models here.
from .models import post
class PostAdmin(admin.ModelAdmin):
    list_display = ['title', 'body','author']
    search_fields =['title']


admin.site.register(post, PostAdmin)
