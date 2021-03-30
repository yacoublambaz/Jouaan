from django.shortcuts import render
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
    form = newCustomerForm()
    #returns the login page
    context = {'form':form}
    return render(request,'main/login.html',context)

def register_view(request):
    #returns register page
    context = {}
    return render(request,'main/register.html',context)
#Hassan Jawad, Karim
def index(request): #main page
    #main page
    pass



#Henri, Firas
def restaurant_view(request,pk):
    #restaurant profile
    pass
