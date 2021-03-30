from django.db import models
from django.contrib.auth.models import User
# Create your models here.

class Customer(models.Model):
    #needs to inherit Django User Model
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    #id
    id = models.IntegerField(primary_key=True)
    #name:
    name = models.CharField(max_length=200)
    #email:
    email = models.CharField(max_length=200)
    #Number of reviews
    #This wouldn't work, instead, we need to filter all reviews
    #depending on Customer id
    #signup date
    signup_date = models.DateTimeField(auto_now_add=True)

class Restaurant(models.Model):
    #inherits from Django User Model
    user = models.OneToOneField(User,null=True,on_delete=models.CASCADE)
    #id
    id = models.IntegerField(primary_key=True)
    #restaurant name
    name = models.CharField(max_length=200)
    #picture
    profile_pic = models.ImageField(null=True)
    #address
    address = models.CharField(max_length=200)
    #telephone number
    phone_number = models.CharField(max_length=8)
    #Reviews -> foreignkey
    #This wouldn't work, instead, we need to filter all reviews
    #depending on restaurant name
    #What we serve?
    what_we_serve = models.CharField(max_length=200)
    #signup date
    signup_date = models.DateTimeField(auto_now_add=True)

class Review(models.Model):
    #id
    id = models.IntegerField(primary_key=True)
    #date auto_add_now
    review_date = models.DateTimeField(auto_now_add=True)
    #customer (who did the review?)
    customer = models.ForeignKey(Customer,on_delete = models.CASCADE)
    #Cleanliness (numbers from 1 to 5)
    cleanliness = models.IntegerField(null=True)
    #Taste
    taste = models.IntegerField(null=True)
    #Environment
    environment = models.IntegerField(null=True)
    #Price
    price = models.IntegerField(null=True)
    #Additional_comments
    comments = models.TextField(null=True)
    #Review out of 5 stars
    review_score = models.IntegerField(null=True)

class Announcement(models.Model):
    #restaurant_id
    restaurant = models.ForeignKey(Restaurant,on_delete = models.CASCADE)
    #text
    text = models.TextField(null=True)
