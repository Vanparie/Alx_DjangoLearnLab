from django.shortcuts import render

from rest_framework.generics import ListAPIView, RetrieveAPIView, CreateAPIView, UpdateAPIView, DestroyAPIView
from rest_framework.filters import SearchFilter, OrderingFilter
from django_filters.rest_framework import OrderingFilter
from django_filters.rest_framework import DjangoFilterBackend

from django_filters import rest_framework
from rest_framework import generics
from .models import Book
from .serializers import BookSerializer

from rest_framework.permissions import IsAuthenticatedOrReadOnly, IsAuthenticated


# ListAPIView: Handles GET requests to retrieve all books
class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

 # Enable filtering, searching, and ordering
    filter_backends = [DjangoFilterBackend, SearchFilter, OrderingFilter]

    # Specify fields for filtering
    filterset_fields = ['title', 'author__name', 'publication_year']

    # Specify fields for searching
    search_fields = ['title', 'author__name']

    # Specify fields for ordering
    ordering_fields = ['title', 'publication_year']


# RetrieveAPIView: Handles GET requests to retrieve a specific book by ID
class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer


class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_create(self, serializer):
        # Example: Set default values or log data during creation
        serializer.save()

class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer

    def perform_update(self, serializer):
        # Example: Log updates or set fields programmatically
        serializer.save()


from rest_framework.permissions import IsAuthenticated, AllowAny

class BookListView(ListAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Public access

class BookDetailView(RetrieveAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [AllowAny]  # Public access

class BookCreateView(CreateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only

class BookUpdateView(UpdateAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only

class BookDeleteView(DestroyAPIView):
    queryset = Book.objects.all()
    serializer_class = BookSerializer
    permission_classes = [IsAuthenticated]  # Authenticated users only


# BookListView handles advanced querying for books.
# Features:
# - Filtering: Use ?field=value to filter results by fields like title, author, and publication_year.
# - Searching: Use ?search=query to search for text in title or author fields.
# - Ordering: Use ?ordering=field or ?ordering=-field to sort by fields like title and publication_year.

# Example API Requests:
# 1. Filter by author: GET /api/books/?author__name=George Orwell
# 2. Search by title: GET /api/books/?search=1984
# 3. Order by publication_year (asc): GET /api/books/?ordering=publication_year
# 4. Order by title (desc): GET /api/books/?ordering=-title

