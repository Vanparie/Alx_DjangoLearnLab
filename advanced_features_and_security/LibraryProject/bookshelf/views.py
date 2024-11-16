from django.shortcuts import render

# bookshelf/views.py

from django.shortcuts import render, get_object_or_404, redirect
from django.contrib.auth.decorators import permission_required
from .models import Book

# Example view for viewing a book
@permission_required('bookshelf.can_view', raise_exception=True)
def view_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    return render(request, 'bookshelf/view_book.html', {'book': book})

# Example view for creating a book
@permission_required('bookshelf.can_create', raise_exception=True)
def create_book(request):
    if request.method == 'POST':
        # Handle form submission to create a book
        pass
    return render(request, 'bookshelf/create_book.html')

# Example view for editing a book
@permission_required('bookshelf.can_edit', raise_exception=True)
def edit_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    if request.method == 'POST':
        # Handle form submission to edit the book
        pass
    return render(request, 'bookshelf/edit_book.html', {'book': book})

# Example view for deleting a book
@permission_required('bookshelf.can_delete', raise_exception=True)
def delete_book(request, book_id):
    book = get_object_or_404(Book, pk=book_id)
    book.delete()
    return redirect('bookshelf:book_list')

