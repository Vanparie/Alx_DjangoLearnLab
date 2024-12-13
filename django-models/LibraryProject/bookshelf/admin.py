from django.contrib import admin

# Register your models here.
from .models import Book

# Register the Book model with customizations
@admin.register(Book)
class BookAdmin(admin.ModelAdmin):
    # Specify fields to display in the list view
    list_display = ('title', 'author', 'publication_year')

    # Add search functionality for title and author fields
    search_fields = ('title', 'author')

    # Add filters for publication year
    list_filter = ('publication_year',)