__author__ = 'Pareng Je'
from django import forms
from django.contrib.auth import authenticate, login

class LoginForm(forms.Form):
    username = forms.CharField(max_length=17,
                               widget=forms.TextInput(attrs={'class': "input100"}))
    password = forms.CharField(max_length=17,widget=forms.PasswordInput(attrs={'class': "input100"}))

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
