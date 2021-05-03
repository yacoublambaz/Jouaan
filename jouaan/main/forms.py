from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer,Restaurant
from django.forms.widgets import FileInput
#Customers Forms Below
class newCustomerForm(UserCreationForm):
    """Creates a new Customer"""
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ("username","email", "password1", "password2")

    def save(self, commit=True):
        user = super(newCustomerForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CustomerForm(ModelForm):
    """Allows Customer to Edit Information"""
    class Meta:
        model=Customer
        fields = '__all__'
        exclude = ['user','id']
        widgets = {
         'profile_pic': FileInput(),
       }


#Restaurant Forms Below
class newRestaurantForm(UserCreationForm):
    """Creates a new Restaurant"""
    email = forms.EmailField(required = True)
    phone_number = forms.CharField(max_length=12)
    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "password1", "password2")

    def save(self, commit=True):
        user = super(newRestaurantForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class RestaurantForm(ModelForm):
    """Allows Restaurant to Edit Information"""
    class Meta:
        model=Restaurant
        exclude = ['user','id']
        widgets = {
         'logo': FileInput(),
         'menu': FileInput(),
         'place': FileInput()
       }
