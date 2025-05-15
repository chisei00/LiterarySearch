from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import UserRegistrationForm


def home(request):
    return render(request, 'users/index.html')

def register(request):
    if request.method == 'POST':
       form = UserRegistrationForm(request.POST)
       if form.is_valid():
               form.save()

               messages.success(request, f'Your account has been created. You can login now!')
               return redirect('login')
    else:
        form = UserRegistrationForm()

        context = {'form' : form}
        return render(request, 'users/register.html', context)
        


# Create your views here.
