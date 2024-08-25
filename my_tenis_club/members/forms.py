from typing import Any
from .models import Useraccount,Person,Members
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate
from django import forms



class Signup(UserCreationForm):
    username=forms.CharField(
        max_length=30,
        widget=forms.TextInput(attrs={'class':'form-control','placeholder':'firstname ...','type':'text','name':'username'})
    )
    # lastname=forms.CharField(
    #     max_length=30,
    #     widget=forms.TextInput(attrs={'class':'form-control','placeholder':'lastname ...','type':'text','name':'lastname'})
    # )
    email=forms.EmailField(
        max_length=30,
        widget=forms.EmailInput(attrs={'class':'form-control','placeholder':'email ...','type':'email','name':'email'})
    )
    # password=forms.CharField(
    #     max_length=30,
    #     widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password ...','type':'password','name':'password'})
    # )
    # password1=forms.CharField(
    #     max_length=30,
    #         widget=forms.PasswordInput(attrs={'class':'form-control','placeholder':'password1 ...','type':'password','name':'password1'})
    # )
    


    class Meta:
        model=Useraccount
        fields=('username','email')

    def clean_email(self):
        email=self.cleaned_data['email'].lower()
        try:
            account=Useraccount.objects.exclude(pk=self.instance.pk).get(email=email)
        except Useraccount.DoesNotExist:
            return email
        raise forms.ValidationError('this email is using')
    
    def clean_username(self):
        username=self.cleaned_data['username']
        try:
            account=Useraccount.objects.exclude(pk=self.instance.pk).get(username=username)
        except Useraccount.DoesNotExist:
            return username
        raise forms.ValidationError('this username is using')



class Search(forms.ModelForm):
    class Meta:
        model = Person
        fields = '__all__'

    # def __init__(self, *args, **kwargs):
    #     super().__init__(*args, **kwargs)
    #     self.fields['name'].queryset = Members.objects.none()

        # if '' in self.data:
        #     try:
        #         country_id = int(self.data.get('country'))
        #         self.fields['city'].queryset = City.objects.filter(country_id=country_id).order_by('name')
        #     except (ValueError, TypeError):
        #         pass  # invalid input from the client; ignore and fallback to empty City queryset
        # elif self.instance.pk:
        #     self.fields['city'].queryset = self.instance.country.city_set.order_by('name')