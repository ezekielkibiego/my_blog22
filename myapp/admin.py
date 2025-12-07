from django.contrib import admin
from .models import Blog, Author, Book, Subscriber

@admin.register(Blog)
class BlogAdmin(admin.ModelAdmin):
    list_display = ('title', 'author', 'created_date', 'published_date')
    
    list_display_links = ('title',)
    
    list_filter = ('author', 'created_date', 'published_date')
    
@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email')
    
    list_display_links = ('email',)
    
    list_filter = ('first_name', 'last_name',)
    
admin.site.register(Book)
admin.site.register(Subscriber)

