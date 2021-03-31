from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import newCustomerForm,CustomerForm,newRestaurantForm,RestaurantForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required

# Create your views here.

#Yacoub
def login_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == "POST":
            form = AuthenticationForm(request = request, data = request.POST)
            if form.is_valid():
                username = form.cleaned_data.get('username')
                password = form.cleaned_data.get('password')
                user = authenticate(username=username,password=password)
                if user is not None:
                    login(request,user)
                    messages.info(request,f"You are now logged in as {username}")
                    return redirect('/')
                else:
                    messages.error(request, 'Invalid Username or Password.')
            else:
                messages.error(request, "Invalid username or password.")
        form = AuthenticationForm()
        #returns the login page
        context = {'form':form}
        return render(request,'main/login.html',context)


def logoutUser(request):
    logout(request)
    return redirect('login')

def register_customer_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = newCustomerForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request,f"New account created: {username}")
                login(request,user)
                return redirect('/')
            else:
                for msg in form.error_messages:
                    messages.error(request, f"{msg}: {form.error_messages[msg]}")
                return render(request,'main/register.html',{'form':form})
        #returns register page
        form = newCustomerForm()
        context = {'form':form}
        return render(request,'main/register.html',context)

def register_restaurant_view(request):
    if request.user.is_authenticated:
        return redirect('/')
    else:
        if request.method == 'POST':
            form = newRestaurantForm(request.POST)
            if form.is_valid():
                user = form.save()
                username = form.cleaned_data.get('username')
                messages.success(request,f"New account created: {username}")
                login(request,user)
                return redirect('/')
            else:
                for msg in form.error_messages:
                    messages.error(request, f"{msg}: {form.error_messages[msg]}")
                return render(request,'main/register.html',{'form':form})
        #returns register page
        form = newRestaurantForm()
        context = {'form':form}
        return render(request,'main/register_restaurant.html',context)
#Hassan Jawad, Karim
def index(request): #main page
    #main page
    pass



#Henri, Firas
def restaurant_view(request,pk):
    #restaurant profile
    pass
