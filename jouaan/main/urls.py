
from django.contrib import admin
from django.urls import path

urlpatterns = [
    path('admin/', admin.site.urls),
    path('register/',views.register_view,name = "register"),
    path('login/',views.login_view,name = "login"),
    path('index/',views.index,name = "index"),
    path('restaurant/<id:pk>',views.restaurant,name = "restaurant")
]
