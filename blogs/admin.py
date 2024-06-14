from django.contrib import admin
from .models import Category, Blog
# Register your models here.

class BlogAdmin(admin.ModelAdmin):
    prepopulated_fields = {'slug': ('title',)}
    list_display = ('author','title', 'category', 'updated_at', 'status', 'created_at')
    search_fields = ('title', 'short_description')     
    list_filter = ('category', 'author') 
    
    
    
admin.site.register(Category)
admin.site.register(Blog, BlogAdmin)