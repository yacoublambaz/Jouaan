from django import forms
from django.forms import ModelForm
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
from .models import Customer,Restaurant
#Customers Forms Below
class newCustomerForm(UserCreationForm):
    """Creates a new Customer"""
    email = forms.EmailField(required = True)
    class Meta:
        model = User
        fields = ("username", "email", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class CustomerForm(ModelForm):
    """Allows Customer to Edit Information"""
    class Meta:
        model=Customer
        fields = '__all__'
        exclude = ['user']


#Restaurant Forms Below
class newRestaurantForm(UserCreationForm):
    """Creates a new Restaurant"""
    email = forms.EmailField(required = True)
    phone_number = forms.CharField(max_length=12)
    class Meta:
        model = User
        fields = ("username", "email", "phone_number", "password1", "password2")

    def save(self, commit=True):
        user = super(NewUserForm, self).save(commit=False)
        user.email = self.cleaned_data["email"]
        if commit:
            user.save()
        return user

class RestaurantForm(ModelForm):
    """Allows Restaurant to Edit Information"""
    class Meta:
        model=Restaurant
        fields = '__all__'
        exclude = ['user']