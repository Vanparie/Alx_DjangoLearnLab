from django import forms
from django.contrib.auth.models import User
from .models import Post

class ProfileForm(forms.ModelForm):
    class Meta:
        model = User
        fields = ['username', 'email', 'first_name', 'last_name']


# Create and Configure Forms

class PostForm(forms.ModelForm):
    class Meta:
        model = Post
        fields = ["title", "content"]  # Only allow editing of title and content
