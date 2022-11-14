from django import forms
from .models import YouTube_Channels

class YouTube_Channel_Form(forms.ModelForm):
    body = forms.CharField(required=True)

    class Meta:
        model = YouTube_Channels
        exclude = ("user", )
