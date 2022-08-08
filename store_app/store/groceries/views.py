from django.shortcuts import render, redirect
from rest_framework import viewsets
from .models import BeautyProducts, Fruits, Vegetables
from .serializers import BeautyProductsSerializer, FruitsSerializer, VegetablesSerializer
from django.views.decorators.http import require_http_methods
from django.contrib import messages
from django.contrib.auth import login, logout, authenticate
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from .forms import UserForm


def index(request):
    if request.method == 'POST':
        username = request.POST.get('username')        
        password = request.POST.get('password')

        try:
            user = authenticate(username = username, password = password)
            if user is not None:
                login(request,user)
                return redirect("api/")
            else:
                messages.success(request, f'Username or password not correct')
                return redirect('index')    
        except Exception as e:
            messages.success(request, f'Username or password not correct {e}')
            return redirect('index')    
    else:
        return render(request, "index.html")


def validate_pass(password):
    msg = ''
    d  = 0
    a = 0
    for j in password:
        if j.isdigit():
            d+=1
        elif j.isalpha():
            a +=1

    if len(password) < 8:
        msg = 'Password should be minimum of 8 characters'
    
    elif d == 0:
        msg = 'Password should contain atleast one digit'

    elif a == 0:
        msg = 'Password should contain atleast one alphabet character'

    return msg


def signup(request):
    if request.method == "POST":
        form = UserForm(request.POST)
        username = form['username'].value()
       
        try:    
            if User.objects.get(username = username) != '':
                messages.success(request, f'username {username} already exists')
                return redirect('signup')
        except:
            pass
        
        password =  form['password'].value()

        val = validate_pass(password)

        if val == '':                 
            if form.is_valid():
                form.save()
                instance = User.objects.get(username = username)
                instance.set_password(password)
                instance.save()
                messages.success(request, 'Your account is succesfully created. you can now sign in')
                return redirect('index')
        else:
            messages.success(request, val)
            return redirect('signup')
    else:
        form = UserForm
    
    data= {
        'form':form,
    }

    return render(request, 'signup.html', data)


def logout_user(request):
    logout(request)
    messages.success(request, 'You have been logged out!!!')
    return redirect('index')


class FruitsViewSet(viewsets.ModelViewSet):
    queryset = Fruits.objects.all()
    serializer_class = FruitsSerializer


class VegetablesViewSet(viewsets.ModelViewSet):
    queryset = Vegetables.objects.all()
    serializer_class = VegetablesSerializer


class BeautyProductsViewSet(viewsets.ModelViewSet):
    queryset = BeautyProducts.objects.all()
    serializer_class = BeautyProductsSerializer

