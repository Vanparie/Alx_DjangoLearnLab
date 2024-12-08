from django.shortcuts import render

from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect
from django.contrib import messages
from .forms import ProfileForm
from django.contrib.auth import login
from django.contrib.auth.models import User
from django.http import HttpResponse

def register(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            return redirect('profile')
    else:
        form = UserCreationForm()
    return render(request, 'registration/register.html', {'form': form})

@login_required
def profile(request):
    return render(request, 'profile.html', {'user': request.user})


def profile_view(request):
    if request.method == 'POST':
        form = ProfileForm(request.POST, instance=request.user)
        if form.is_valid():
            form.save()
            messages.success(request, 'Your profile has been updated successfully!')
            return redirect('profile')
        else:
            messages.error(request, 'Please correct the error below.')
    else:
        form = ProfileForm(instance=request.user)

    return render(request, 'profile.html', {'form': form})