from django import forms
from .models import *



class EnquiryForm(forms.ModelForm):
    class Meta:
        model = client_enquery
        fields = '__all__'