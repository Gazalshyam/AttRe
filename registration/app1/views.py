from django.shortcuts import render,redirect
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .models import Feature
from .forms import  Reg_form

# Create your views here.
@login_required(login_url='login')

def HomePage(request):
    return render (request,'home.html')



def SignupPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        email=request.POST.get('email')
        password=request.POST.get('password1')
        password2=request.POST.get('password2')
        # print(username,email,password,password2)

        if password == password2:
            if User.objects.filter(email=email).exists():
                messages.info(request,'Email already exists')
                return redirect('signup')

            elif User.objects.filter(username=username).exists():
                messages.info(request,'#Username already exists')
                return redirect('signup')
            else :
                user=User.objects.create_user(username=username, email=email,password=password)
                user.save()
                return redirect('login')
        else:
            messages.info(request, 'Passwords do not match')
            return redirect('signup')
    else:
        return render(request, 'signup.html')

def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        print(username,pass1)
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('form')
        else:
            messages.info("Username or Password is incorrect!!!")
            return redirect('login')

    return render (request,'login.html')

def LogoutPage(request):
    logout(request)
    return redirect('login')


def Form(request):
    submitted=False
    if request.method=='POST':
        form = Reg_form(request.POST)
        if form.is_valid():
            form.save()
            # print(form)
            submitted = True
            messages.info('Successfully Saved')
            return render(request,'home.html')
        else:
            form = Reg_form()
            # print(form)
            messages.info('Form validation failed')
            return render(request,'form.html',{'form':form})
    form=Reg_form()
    # print(Reg_form)
    return render(request,'form.html',{'form':form})


