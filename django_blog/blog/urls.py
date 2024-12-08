from django.urls import path, include
from . import views
from .views import profile_view
from .views import (
    PostListView, 
    PostDetailView, 
    PostCreateView, 
    PostUpdateView, 
    PostDeleteView
)

urlpatterns = [
    path('login/', include('django.contrib.auth.urls')),  # Handles login and logout views
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/', profile_view, name='profile'),
    path('login/', views.login_view, name='login'),
    path('', PostListView.as_view(), name='post-list'),
    path('post/<int:pk>/', PostDetailView.as_view(), name='post-detail'),
    path('post/new/', PostCreateView.as_view(), name='post-create'),
    path('post/<int:pk>/update/', PostUpdateView.as_view(), name='post-update'),  # Updated URL pattern for the update view
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
    path('post/<int:post_id>/', views.post_detail, name='post-detail'),
    path('post/<int:pk>/comments/new/', views.add_comment, name='add-comment'),
    path('comment/<int:pk>/update/', views.edit_comment, name='edit-comment'),
    path('comment/<int:pk>/delete/', views.delete_comment, name='delete-comment'),
]
