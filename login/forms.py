__author__ = 'Pareng Je'
from django import forms
from django.contrib.auth import authenticate, login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.models import User
class LoginForm(forms.Form):
    username = forms.CharField(max_length=17,error_messages={'required': '*'},
                               widget=forms.TextInput(attrs={'class': "input100"}))
    password = forms.CharField(max_length=17,error_messages={'required': '*'},widget=forms.PasswordInput(attrs={'class': "input100"}))

    def clean(self):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        if not user or not user.is_active:
            raise forms.ValidationError("Sorry, that login was invalid. Please try again.")
        return self.cleaned_data

    def login(self, request):
        username = self.cleaned_data.get('username')
        password = self.cleaned_data.get('password')
        user = authenticate(username=username, password=password)
        return user

class RegisterForm(UserCreationForm):
    username = forms.CharField(max_length=17,required=False ,widget=forms.TextInput(attrs={'class':'form-control'}))
    first_name = forms.CharField(max_length=50, required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    last_name = forms.CharField(max_length=50, required=False,widget=forms.TextInput(attrs={'class':'form-control'}))
    # password1 = forms.CharField(max_length=25, required=False,min_length=10 ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    email = forms.EmailField(max_length=35, required=False,widget=forms.EmailInput(attrs={'class':'form-control'}))
    # password2 = forms.CharField(max_length=25, required=False,min_length=10 ,widget=forms.PasswordInput(attrs={'class':'form-control'}))
    
    class Meta:
        model = User
        fields = ['username','first_name', 'last_name','email','password1', 'password2']

     #validation is taken over by the Parent Class
