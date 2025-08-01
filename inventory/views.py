from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate

# Create your views here.

def signup(request):

  if request.method == 'GET':
    return render(request, 'sign_up.html', {
      'form': UserCreationForm()
      })
  else:
    if request.POST['password1'] == request.POST['password2']:
      # register user
      try:
        user = User.objects.create_user(
        username=request.POST['username'],
        password=request.POST['password1']
        )
        print(request.POST)
        user.save()
        login(request, user)
        return redirect('home')
      except:
        return render(request, 'sign_up.html', {
      'form': UserCreationForm(),
      'error': 'Username already exists'
      })
    return render(request, 'sign_up.html', {
      'form': UserCreationForm(),
      'error': 'Passwords do not match'
    })
  

def home(request):
  return render(request, 'home.html', {
    'message': 'Welcome to mepersoft, this is the inventory management system'
  })