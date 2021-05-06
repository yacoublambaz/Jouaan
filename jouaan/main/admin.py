from django.contrib import admin
from .models import Customer,Restaurant,Review,Announcement,Complaint
# Register your models here.

admin.site.register(Customer)
admin.site.register(Restaurant)
admin.site.register(Review)
admin.site.register(Announcement)
admin.site.register(Complaint)
