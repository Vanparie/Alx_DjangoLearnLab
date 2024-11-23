from django.shortcuts import render

from rest_framework.generics import ListAPIView
from generics.ListAPIView import ListAPIView
from .models import Book
from .serializers import BookSerializer

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Fetch all Book instances
    serializer_class = BookSerializer  # Use the serializer
