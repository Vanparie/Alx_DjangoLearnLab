from django.shortcuts import render

from django import forms

from .models import Book

class SearchForm(forms.Form):
    query = forms.CharField(max_length=100, required=False)

# In your view:
from .forms import SearchForm

def search_books(request):
    form = SearchForm(request.GET)
    if form.is_valid():
        query = form.cleaned_data['query']
        books = Book.objects.filter(title__icontains=query)
    return render(request, 'bookshelf/book_list.html', {'form': form, 'books': books})


class ExampleForm(forms.Form):
    name = forms.CharField(max_length=100, label='Your Name')
    email = forms.EmailField(label='Your Email')
    age = forms.IntegerField(min_value=0, label='Your Age')