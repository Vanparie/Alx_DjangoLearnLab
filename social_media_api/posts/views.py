from django.shortcuts import render

from rest_framework import viewsets, permissions
from .models import Post, Comment
from .serializers import PostSerializer, CommentSerializer

class PostViewSet(viewsets.ModelViewSet):
    queryset = Post.objects.all().order_by('-created_at')
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


class CommentViewSet(viewsets.ModelViewSet):
    queryset = Comment.objects.all().order_by('-created_at')
    serializer_class = CommentSerializer
    permission_classes = [permissions.IsAuthenticatedOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author=self.request.user)


#posts/views.py (Enhanced)

from rest_framework import filters
from rest_framework.pagination import PageNumberPagination

class PostPagination(PageNumberPagination):
    page_size = 10

class PostViewSet(viewsets.ModelViewSet):
    ...
    pagination_class = PostPagination
    filter_backends = [filters.SearchFilter]
    search_fields = ['title', 'content']

