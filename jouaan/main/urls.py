
from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('register/',views.register_view,name = "register"),
    path('login/',views.login_view,name = "login"),
    path('index/',views.index,name = "index"),
    path('restaurant/<str:pk>/',views.restaurant_view,name = "restaurant")
]
