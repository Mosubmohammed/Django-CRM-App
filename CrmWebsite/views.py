from django.shortcuts import redirect, render
from django.contrib.auth import authenticate,login,logout
from django.contrib import messages

# Create your views here.

def home(request):
    if request.method =="POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(request,username=username, password=password)
        if user is not None:
            login(request, user)
            messages.success(request, 'Welcome back!!')
            
            return redirect('home')
        else:
            messages.success(request, 'Invalid username or password!!')
            return redirect('home')
    else:
        return render(request,'home.html',{})



def logout_user(request):
    logout(request)
    messages.success(request, 'You Have been logged out!!')
    
    return redirect('home')
