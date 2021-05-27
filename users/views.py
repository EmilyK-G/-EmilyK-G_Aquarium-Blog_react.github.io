from django.shortcuts import render, redirect
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import UserRegisterForm

def login(request):
    return render(request, 'users/login.html', {'page_name': 'login'})

def register(request):
   
    if request.method == 'POST':
        form = UserRegisterForm(request.POST)
        if form.is_valid():
            form.save()
            username = form.cleaned_data.get('username')
            messages.success(request, f'Welcome to the team {username}! Login to share your fishkeeper life')
            return redirect('login')
    else:
        form = UserRegisterForm()
    return render(request, 'users/register.html', {'form': form, 'page_name': 'register'})


#@login_required
# def profile(request):
#     return render(request, 'users/profile.html')