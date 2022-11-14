from django import forms
from django.contrib.auth import authenticate
from account.models import accounts



class AccountAuthenticationForm(forms.ModelForm):
    class Meta:
        model = accounts
        fields = ('email', 'password')
    
    def clean(self):
        if self.is_valid():
            email = self.cleaned_data['email']
            password = self.cleaned_data['password']
            if not authenticate(email=email, password=password):
                raise forms.ValidationError("Invalid login")
