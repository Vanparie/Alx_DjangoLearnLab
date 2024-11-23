from django.shortcuts import render

from rest_framework.generics import ListAPIView
from generics.ListAPIView import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Fetch all Book instances
    serializer_class = BookSerializer  # Use the serializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer for formatting the response    
