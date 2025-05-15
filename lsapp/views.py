from django.shortcuts import render, redirect
from django.contrib.auth import login, authenticate
from django.contrib import messages
from django.contrib.auth.forms import UserCreationForm
from .forms import RegistrationForm


def home(request):
    return render(request, 'users/index.html')

def register(request):
    form = RegistrationForm()

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
                form.save()
                
                messages.success(request, '🎉Account created!🎉')
                return redirect('login')
    else:
         form = RegistrationForm()

    context = {'form' : form}
    return render(request, 'users/register.html', context)

#    if request.method == 'POST':
#       form = RegistrationForm(request.POST)
#       if form.is_valid():
#               form.save()

               #messages.success(request, f'Your account has been created. You can login now!')
#               return render('users/register.html')
#    else:
#        form = RegistrationForm()

#        context = {'form' : form}
#        return render(request, 'users/register.html', context)


# Create your views here.
