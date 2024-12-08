from django.urls import path, include
from . import views
from .views import profile_view

urlpatterns = [
    path('login/', include('django.contrib.auth.urls')),  # Handles login and logout views
    path('register/', views.register, name='register'),
    path('profile/', views.profile, name='profile'),
    path('profile/', profile_view, name='profile'),
]
