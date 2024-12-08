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
    path('post/<int:pk>/edit/', PostUpdateView.as_view(), name='post-update'),
    path('post/<int:pk>/delete/', PostDeleteView.as_view(), name='post-delete'),
]
