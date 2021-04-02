from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import newCustomerForm,CustomerForm,newRestaurantForm,RestaurantForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
# Create your views here.

#Yacoub
@unauthenticated_user
def login_view(request):
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
    list(messages.get_messages(request))
    return redirect('login')

@unauthenticated_user
def register_customer_view(request):
    if request.method == 'POST':
        form = newCustomerForm(request.POST)
        
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            messages.success(request,f"Hello, {username}, your account has been created!")
            return redirect('login')
        else:
            for msg in form.error_messages:
                messages.error(request, f" {form.error_messages[msg]}")
            return render(request,'main/register.html',{'form':form})
    #returns register page
    form = newCustomerForm()
    context = {'form':form}
    return render(request,'main/register.html',context)

@unauthenticated_user
def register_restaurant_view(request):
    
    if request.method == 'POST':
        form = newRestaurantForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')
            group = Group.objects.get(name='restaurant')
            user.groups.add(group)
            messages.success(request,f"Hello, {username}, your account has been created!")
            return redirect('login')
        else:
            for msg in form.error_messages:
                messages.error(request, f" {form.error_messages[msg]}")
            return render(request,'main/register_rest.html',{'form':form})
    #returns register page
    form = newRestaurantForm()
    context = {'form':form}
    return render(request,'main/register_rest.html',context)

    
#Hassan Jawad, Karim
def index(request): #main page
    return render(request,'main/index.html',context = {})



#Henri, Firas
#@allowed_users(allowed_roles = ['restaurant','customer'])
def restaurant_view(request,pk):
    #restaurant profile
    pass
