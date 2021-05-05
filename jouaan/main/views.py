from django.shortcuts import render, redirect
from django.contrib.auth.forms import UserCreationForm,AuthenticationForm
from .forms import newCustomerForm,CustomerForm,newRestaurantForm,RestaurantForm,ReviewForm,AnnouncementForm
from django.contrib import messages
from django.contrib.auth import login
from django.contrib.auth import logout
from django.contrib.auth import authenticate
from django.contrib.auth.decorators import login_required
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group
from .models import Customer, Restaurant, Review, Announcement
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
            email = form.cleaned_data.get('email')
            group = Group.objects.get(name='customer')
            user.groups.add(group)
            Customer.objects.create(
                user=user,
                name=username,
                email = email
            )
            messages.success(request,f"Hello, {username}, your account has been created!")
            return redirect('login')
        else:
           
            for msg in form.error_messages:
                
                messages.error(request, f" {form.error_messages[msg]} or your password is too common")
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
            phone = form.cleaned_data.get('phone_number')
            email = form.cleaned_data.get('email')
            user.groups.add(group)
            Restaurant.objects.create(
                user = user,
                name = username,
                phone_number = phone,
                email = email,
                review_score = 4,
            )
            messages.success(request,f"Hello, {username}, your account has been created!")
            return redirect('login')
        else:
            
            for msg in form.error_messages:

                messages.error(request, f" {form.error_messages[msg]} or your password is too common")
            return render(request,'main/register_rest.html',{'form':form})
    #returns register page
    form = newRestaurantForm()
    context = {'form':form}
    return render(request,'main/register_rest.html',context)

    
#Hassan Jawad, Karim
def index(request): #main page
    restaurants = Restaurant.objects.all()
    announcements = Announcement.objects.all()[:20]
    context = {'restaurants':restaurants,'announcements':announcements}
    return render(request,'main/index.html',context)

def reviews(request):
    restaurants = Restaurant.objects.all()
    announcements = Announcement.objects.all()[:20]
    context = {'restaurants':restaurants,'announcements':announcements}
    return render(request,'main/review.html',context)

@login_required(login_url='login')
def update(request):
    customer = request.user.customer
    form = CustomerForm(instance=customer)
    if request.method == 'POST':
        form = CustomerForm(request.POST,request.FILES, instance=customer)
        
        if form.is_valid():
            
            form.save()
      
    context = {'form':form}
    return render(request,"main/update.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles = ['restaurant'])
def update_restaurant(request):
    restaurant = request.user.restaurant
    form = RestaurantForm(instance = restaurant)
    if request.method == 'POST':
        
        form = RestaurantForm(request.POST,request.FILES,instance=restaurant)
        
        if form.is_valid():
            form.save()
    context={'form':form}
    return render(request,"main/restaurant_update.html",context)

@login_required(login_url='login')
@allowed_users(allowed_roles = ['restaurant'])
def announcements(request):
    restaurant = request.user.restaurant
    form = AnnouncementForm()
    if request.method == 'POST':
        form = AnnouncementForm(request.POST)
        if form.is_valid():
            Announcement.objects.create(restaurant = restaurant, text = form.cleaned_data.get('text'))
            return redirect('index')
    context={'form':form}
    return render(request,"main/announcement.html",context)
#Henri, Firas
#@allowed_users(allowed_roles = ['restaurant','customer'])

def restaurant_view(request, pk):
    restaurant = Restaurant.objects.get(id = pk)
    review = Review.objects.filter(restaurant_id = pk)[:20]
    current_total = 0
    current_count = 0
    for rev in review:
        if rev.review_score:
            current_total += rev.review_score
            current_count += 1
    form = ReviewForm()
    if request.method == 'POST':
        form = ReviewForm(request.POST)
        if form.is_valid():
            cleanliness = form.cleaned_data.get('cleanliness')
            taste = form.cleaned_data.get('taste')
            environment = form.cleaned_data.get('environment')
            price = form.cleaned_data.get('price')
            comments = form.cleaned_data.get('comments')
            total = (int(cleanliness) + int(taste) + int(environment) + int(price))/4
            total = round(total)
            Review.objects.create(
                customer = request.user.customer,
                restaurant_id = pk,
                cleanliness=cleanliness,
                price = price,
                environment = environment,
                taste = taste,
                comments = comments,
                review_score = total,
            )
            current_total += total
            current_count += 1
            new_review_score = current_total/current_count
            resto = Restaurant.objects.filter(id = pk).update(review_score = new_review_score)
            return redirect('index')

            
    return render(request,"main/restaurant.html",context= {'form':form,'review':review,'restaurant':restaurant})

def search_restos(request):
    if request.method == 'POST':
        searched = request.POST['searched']
        restos = Restaurant.objects.filter(name__contains=searched)
        context={'searched':searched,'restos':restos}

        return render(request,"main/search_restos.html",context)
    else:
        context={}
        return render(request,"main/search_restos.html",context)