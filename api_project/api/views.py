from django.shortcuts import render

from rest_framework.generics import ListAPIView
from generics.ListAPIView import ListAPIView
from .models import Book
from .serializers import BookSerializer
from rest_framework import viewsets

from rest_framework.authtoken.views import obtain_auth_token
from rest_framework.permissions import IsAuthenticated

class BookList(ListAPIView):
    queryset = Book.objects.all()  # Fetch all Book instances
    serializer_class = BookSerializer  # Use the serializer

class BookViewSet(viewsets.ModelViewSet):
    queryset = Book.objects.all()  # Retrieve all books
    serializer_class = BookSerializer  # Use the BookSerializer for formatting the response    
    permission_classes = [IsAuthenticated]  # Restrict access to authenticated users