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



# Implement the Feed Functionality


from rest_framework import generics, permissions
from .models import Post
from .serializers import PostSerializer
from posts.serializers import PostSerializer

class FeedView(generics.ListAPIView):
    serializer_class = PostSerializer
    permission_classes = [permissions.IsAuthenticated]


    def get(self, request, *args, **kwargs):
        """
        Return posts from users the current user is following, ordered by creation date.
        """
        # Get the users the current user is following
        following_users = request.user.following.all()

        # Filter posts where the author is in the list of following users
        posts = Post.objects.filter(author__in=following_users).order_by('-created_at')  # Order by most recent first
        
        # Serialize the posts and return the response
        serializer = self.get_serializer(posts, many=True)
        return Response(serializer.data)

    def get_queryset(self):
        user = self.request.user
        followed_users = user.following.all()
        return Post.objects.filter(author__in=followed_users).order_by('-created_at')
