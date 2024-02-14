from django.shortcuts import render
from django.contrib.auth import logout
from django.shortcuts import redirect
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.contrib.auth.forms import AuthenticationForm
from django.http import HttpResponseRedirect

def home(request):
    return render(request, 'home.html')

def logout_view(request):
    logout(request)
    return redirect('/')

def login_view(request):
    """how we login to our app"""
    if request.method == 'POST':
        form = AuthenticationForm(request, request.POST)
        if form.is_valid():
            u = form.cleaned_data['username']
            p = form.cleaned_data['password']
            user = authenticate(username=u, password=p)
            if user is not None:
                pass
                if user.is_active:
                    login(request, user)
                    return HttpResponseRedirect(f'/User/{u}')
                else:
                    print(f'{u} - account has been disabled')
                    return HttpResponseRedirect('/login')
            else:
                print('The username and/or password is incorrect')
                return HttpResponseRedirect('/login')
        else:
            return HttpResponseRedirect('/login')
    else:
        form = AuthenticationForm()
        return render(request, 'login.html', { 'form': form })

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            
            login(request, user)
            return HttpResponseRedirect('/polls')
        else:
            return HttpResponseRedirect('/signup')
    else:
        form = UserCreationForm()
        return render(request, 'signup.html', {'form': form})
    
@login_required
def profile(request, username):
    user = User.objects.get(username=username)
    return render(request, 'profile.html', {'user': user})