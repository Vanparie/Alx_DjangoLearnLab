from django.shortcuts import render
from .forms import ExampleForm

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


def search_books(request):
    query = request.GET.get('q', '')
    if query:
        books = Book.objects.filter(title__icontains=query)
    else:
        books = Book.objects.all()
    return render(request, 'bookshelf/book_list.html', {'books': books})

# bookshelf/views.py

from django.http import HttpResponse

def book_list(request):
    response = render(request, 'bookshelf/book_list.html')
    response['Content-Security-Policy'] = "default-src 'self'; script-src 'self' 'unsafe-inline';"
    return response


def example_view(request):
    if request.method == 'POST':
        form = ExampleForm(request.POST)
        if form.is_valid():
            # Handle the valid form (e.g., save to database, send email, etc.)
            name = form.cleaned_data['name']
            email = form.cleaned_data['email']
            age = form.cleaned_data['age']
            # Add any other processing as required
            return render(request, 'bookshelf/thank_you.html', {'name': name})
    else:
        form = ExampleForm()

    return render(request, 'bookshelf/form_example.html', {'form': form})