from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from account.models import accounts
from .models import *
from influencer.models import YouTube_Channels, Facebook_Page, Instagram_Page
from .forms import EnquiryForm
import random
from django.contrib import messages
from django.core.mail import send_mail



def client_enquiry(request):
    if request.POST:
        form = EnquiryForm(request.POST)
        if form.is_valid():
            form.save()
            clientEmail = form['email'].value()
            send_mail('Thank for your Enquiry - Intromoment', 'Thank for your Enquiry, Will Connect Shortly', 'officialcart24.in@gmail.com', [clientEmail])

            messages.info(request , "THANKYOU ! We are connect with you soon")
            return redirect('home:home')
        else:
            msg=f"{form.errors}"
            messages.info(request , msg)
            return redirect('client:enquiry-form')
            
    YTCategories = YouTube_Channels.objects.all().values('category').distinct()
    FBCategories = Facebook_Page.objects.all().values('category').distinct()
    InstaCategories = Instagram_Page.objects.all().values('category').distinct()

    context={'categories':YTCategories, 'FBCategories':FBCategories, 'InstaCategories':InstaCategories}            
    return render(request , 'Enquiry/enquiry.html',context)
    