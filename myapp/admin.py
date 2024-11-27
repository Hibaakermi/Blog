from django.contrib import admin
from .models import BlogPost, Author

@admin.register(Author)
class AuthorAdmin(admin.ModelAdmin):
    pass  

@admin.register(BlogPost)
class BookAdmin(admin.ModelAdmin):
    list_display = ("title", "content", "author", ) 
    list_editable = ("title",) 
    list_display_links = ("content",)  
    search_fields = ("title",) 
    list_filter = ("author",)  
    list_per_page = 10