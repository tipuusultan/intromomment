from django.urls import path
from .views import *


app_name = 'client'


urlpatterns = [
    path('enquiry-form/' , client_enquiry , name="enquiry-form")
]
