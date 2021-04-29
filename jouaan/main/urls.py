
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_customer_view,name = "register"),
    path('register-rest/',views.register_restaurant_view,name = "register-restaurant"),
    path('login/',views.login_view,name = "login"),
    path('logout/',views.logoutUser,name="logout"),
    path('',views.index,name = "index"),
    path('restaurant/',views.restaurant_view,name = "restaurant"),
    path('update',views.update,name="update")
]
