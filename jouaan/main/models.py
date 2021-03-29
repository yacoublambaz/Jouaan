from django.db import models

# Create your models here.

class Customer(models.Model):
    #needs to inherit Django User Model
    #id
    #name: 
    #email:
    #Number of reviews
    #signup date

class Restaurant(models.Model):
    #inherits from Django User Model
    #id
    #picture
    #restaurant name
    #address
    #telephone number
    #Reviews -> foreignkey
    #What we serve?

class Review(models.Model):
    #id
    #date auto_add_now
    #restaurant (What restaurant is this reviewing?)
    #customer (who did the review?)
    #Cleanliness (numbers from 1 to 5)
    #Taste
    #Environment
    #Price
    #Additional_comments
    #Review out of 5 stars

class Announcement(models.Model):
    #restaurant_id
    #text
