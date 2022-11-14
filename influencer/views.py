from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from account.models import accounts
from .models import *
import random
from django.contrib import messages
from django.contrib.auth import authenticate,logout as deauth, login  as dj_login
from django.conf import settings 
from django.core.mail import send_mail

from influencer.models import *
# Create your views here.

def send_otp(email , otp):
    pass


def check_email(request):
    if request.method == 'POST':
        get_email =request.POST.get('email')
        
        if accounts.objects.filter(email=get_email).exists():
            return HttpResponse(f"""
                        <div id='Msg' class='text-danger'>
                            <p>This Email Already Exist</p>
                        </div>""")
        
        
        else:
            # accounts.objects.filter(email=get_email).update(otp=random.randint(1000,9999))
            otp=random.randint(1000 , 9999)
            request.session['reg_otp'] = otp
            print("OTP",otp)
            send_mail('OTP from Intromoment Influencer Register', f'YOur OTP from Intromoment is {otp}', 't4technology09@gmail.com', recipient_list=[get_email])
            
            
            return HttpResponse(f"""
                                <div id='Msg'>
                                        <div class="form-group mt-1">
                                               <p class='text-success'>An Otp  has been sent to your email</p>
                                            </div>
                                        
                                        </div>                                        
                                        
                                        
                                        <div class="form-group mt-3">
                    
                                                <div class="">
                                                    <input  
                                                            type="text" 
                                                            name="otp" 
                                                            class="form-control"
                                                            placeholder="Enter OTP"
                                                            hx-post="/check-otp/" 
                                                            hx-target="#OTPMsg" 
                                                            hx-trigger="keyup delay:2s"
                                                    >
                                                </div>

                                                <div id="OTPMsg">

                                                </div>

                                        </div>
                                
                                </div>
                                
                                """)
                
def check_otp(request):
    if request.method == 'POST':
        get_otp =request.POST.get('otp')
        reg_otp = request.session.get('reg_otp')
        if get_otp == str(reg_otp):
            return HttpResponse(f"""
                        <div id='OTPMsg' class='text-success'>
                              <div class="form-group row mt-3">
                                            <div class="col-md-4">
                                            </div>
                                            
                                            <div class="col-md-6"> 
                                            <p class='text-success'>Otp is correct</p>
                                            </div>
                                        
                                </div>          
                        </div>""")
        
        else:
            return HttpResponse(f"""
                        <div id='OTPMsg' class='text-danger'>
                              <div class="form-group row mt-3">
                                            <div class="col-md-4">
                                            </div>
                                            
                                            <div class="col-md-6"> 
                                            <p class='text-danger'>Otp is Incorrect</p>
                                            </div>
                                        
                                </div>          
                        </div>""")

def influencer_register(request):
    if request.method == 'POST':
        get_email       = request.POST.get('email')
        get_otp         = request.POST.get('otp')
        get_password1   = request.POST.get('password1')
        get_password2   = request.POST.get('password2') 
        get_name        = request.POST.get('username')

        reg_otp = request.session.get('reg_otp')

        if not get_email:
            return JsonResponse({"status":"Enter Email"})

        if accounts.objects.filter(email=get_email).exists():
            return JsonResponse({"status":"Email Already Exist"})    

        if not  get_otp == str(reg_otp):
            return JsonResponse({"status":"Invalid OTP"})

        if not get_password1 == get_password2:
            return JsonResponse({"status":"Password Not Matched"})

        if len(get_password1) < 4:
            return JsonResponse({"status":"Password Must be 4 Character Long"})     

        
        
        get_obj=accounts.objects.create(username=get_name , email=get_email)
        get_obj.set_password(get_password1)
        get_obj.save()

        influencer_profile.objects.create(
            user = get_obj,
            name = get_name        )

        user = authenticate(email=get_email , password=get_password1)

        dj_login(request , user)
        
        return redirect('influencer:influencer-register-step2')    

    return render(request, 'register/register.html')



def influencer_register_step2(request):
    if request.method == 'POST':
        fb_url       = request.POST.get('fb_url')
        fb_category      = request.POST.get('fb_category')

        yt_url         = request.POST.get('yt_url')
        yt_category        = request.POST.get('yt_category')

        insta_url   = request.POST.get('insta_url')
        insta_category   = request.POST.get('insta_category')

        influencer = influencer_profile.objects.get(user=request.user)

        influencer.Instagram_page_url = insta_url
        influencer.Instagram_page_category = insta_category

        influencer.Facebook_page_url = fb_url
        influencer.Facebook_page_category = fb_category

        influencer.Youtube_channel_url = yt_url
        influencer.Youtube_channel_category = yt_category
        influencer.save()

        messages.success(request, 'Your Account has been created successfully. Our Team will verify your profile')
        return redirect('home:home')    

    return render(request, 'register-step-2.html')


def login(request):
    if request.method == 'POST':
        email = request.POST.get('email')
        password = request.POST.get('password')

        user = authenticate(email=email, password=password)
        try:
            dj_login(request, user)
        except ValueError:
            messages.info(request, "Check your Login Creds")
        

    return render(request, 'login/login.html')

def logout(request):
	if request.user.is_authenticated:
		deauth(request)
	messages.info(request , 'You are Logout Successfully')
	return redirect('home:home')


def add_youtube(request):
    if request.method == 'POST':
        import requests
        from bs4 import BeautifulSoup
        from termcolor import colored

        InputCategory = request.POST.get('category')

        # this is for hong kong
        # ChannelCrawlerCategories = {'Education':'876973', 'Entertainment':'980862', 'Film and Animation':'982376','Gaming':'964607','Howto & Style':'982377','Music':'982379', 'News & Politics':'982381','People & Blogs':'966857','Pets & Animals':'982385', 'Science & Technology':'928708', 'Sports':'344310','Travel & Events':'982386'}
 
        # this is for china
        # ChannelCrawlerCategories = {'Education':'415768', 'Entertainment':'318110', 'Film and Animation':'1002164','Gaming':'487346','Howto & Style':'670275','Music':'313018', 'News & Politics':'403758','People & Blogs':'296935','Pets & Animals':'501791', 'Science & Technology':'369011', 'Sports':'1006287','Travel & Events':'1028987'}

        # this is for Macau
        # ChannelCrawlerCategories = {'Education':'1029090', 'Entertainment':'1029092', 'Film and Animation':'1029093','Gaming':'1014991','Howto & Style':'1029097','Music':'1029098', 'News & Politics':'812474','People & Blogs':'1029100','Pets & Animals':'1029102', 'Science & Technology':'1029103', 'Sports':'367610','Travel & Events':'1029104'}
     
        # this is for Taiwan
        ChannelCrawlerCategories = {'Education':'750311', 'Entertainment':'722407', 'Film and Animation':'750496','Gaming':'391843','Howto & Style':'632851','Music':'1029112', 'News & Politics':'750516','People & Blogs':'678956','Pets & Animals':'1029113', 'Science & Technology':'496828', 'Sports':'1029115','Travel & Events':'1029117'}


        Category = ChannelCrawlerCategories.get(InputCategory)
        print(colored('Searching Channels for ', 'red'), colored(InputCategory, 'green'),colored('.........'))

        r= requests.get(f'https://channelcrawler.com/eng/results2/{Category}/')
        html = BeautifulSoup(r.text, 'html.parser')
        pagination = html.select('.pagination')

        for p in pagination:
            LastPage = p.select('a')[-2].get_text()

        AllChannels = []
        AllChannelsLinks = []
        for i in range(1, int(LastPage)+1):
            new_r= requests.get(f'https://channelcrawler.com/eng/results2/{Category}/page:{i}')
            new_html = BeautifulSoup(new_r.text, 'html.parser')
            channels = new_html.select('.channel')
            for channel in channels:
                title = channel.select('a')[0].get_text()
                link = channel.select('a')[0]['href']
                AllChannels.append(title)
                AllChannelsLinks.append(link)
                if not YouTube_Channels.objects.filter(url=link, category=InputCategory).exists():
                    getchannel = YouTube_Channels(url=link, category=InputCategory, location='Taiwan')
                    getchannel.save()
                else:
                    print("Data Exits")
                print(colored(f'{len(AllChannels)} results found','red'))

        print(AllChannels)
        print(AllChannelsLinks)
        context = {"form": "form"}


    context = {"form": "form"}
    return render(request, 'add_yt_channel.html', context)

def ProfileSettings(request):
    # Influencer = influencer_profile.objects.all()
    if request.user.is_admin:
        messages.info(request,"Profile Settings is not for Admin")
        return redirect('/')
    Influencer = influencer_profile.objects.filter(user=request.user)
    
    context = {'influencer':Influencer}
    return render(request, 'profile-settings.html', context) 

def StoreInfluencer(request):
    from requests_html import HTMLSession
    from selenium import webdriver
    import nest_asyncio
    from pandas import read_excel

    my_sheet = 'sheet1' # change it to your sheet name, you can find your sheet name at the bottom left of your excel file
    file_name = './output/top1000ytchannels.xlsx' # change it to the name of your excel file
    df = read_excel(file_name, sheet_name = my_sheet)
    AllUsers = df['Channel Name'].tolist()
    AllCategories = df['Category'].tolist()
    AllURLS = df['URL'].tolist()
    # url = 'https://hypeauditor.com/top-instagram-all-hong-kong/'
    # LOGIN_URL = 'https://hypeauditor.com/login/'


    # session = HTMLSession()
    # r = session.get(url)
    # r.html.arender()
    # pages = r.html.find('.pager__button', first=False)
    # NoOfPages = []

    # for page in pages:
    #     NoOfPages.append(page)

    # lastPage = NoOfPages[-2].text
    # print(lastPage)


    # driver = webdriver.Chrome('C:/chromedriver.exe')
    # driver.get(LOGIN_URL)   

    # Email_Field = driver.find_element_by_xpath('//*[@id="email"]')
    # Pass_Field = driver.find_element_by_xpath('//*[@id="password"]')
    # submit_btn = driver.find_element_by_xpath('//*[@id="login-form-wrap"]/form[1]/button')

    # Email_Field.send_keys('hey.tipusultan@gmail.com')
    # Pass_Field.send_keys('TIPUsultan')
    # submit_btn.click()

    # AllUsers = []
    # AllCategorie = []

    # for i in range(1,int(lastPage)+1):
    #     AllCat = []
        
    #     NEW_URL = f'{url}?p={i}'
    #     driver.get(NEW_URL)
    #     username = driver.find_elements_by_class_name('contributor__name-content')
    #     for user in username:
    #         AllUsers.append(user.text)
        
    #     for sn in range(2,52):
    #         category = driver.find_elements_by_xpath(f'//*[@id="__layout"]/div/div[1]/div/div[2]/div/div[2]/div/div[{sn}]/div[1]/div[3]/div')
    #         AllCat.append(category)

    #     for c in AllCat:
    #         if len(c) == 0:
    #             AllCategorie.append('No Category')

    #         else:
    #             text = c[0].text
    #             print(text)
    #             AllCategorie.append(text)

    # print(AllUsers[10])
    # print(AllCategorie[10])
    # print("//////////")
    # print(AllUsers[10])
    # print(AllCategorie[10])

    for user in range(0, len(AllUsers)):
        finalURL = AllURLS[user].split('/')[-2]
        if AllCategories[user] == 'Movies':
            category = 'Entertainment'

        if AllCategories[user] == 'Animation':
            category = 'Film and Animation'

        if AllCategories[user] == 'Daily vlogs':
            category = 'Travel & Events'

        if AllCategories[user] == 'Music & Dance':
            category = 'Music'

        if AllCategories[user] == 'Health & Self Help':
            category = 'Education'
        
        if AllCategories[user] == 'Food & Drinks':
            category = 'People & Blogs'
        
        if AllCategories[user] == 'Humor':
            category = 'Travel & Events'

        if AllCategories[user] == 'Travel':
            category = 'Travel & Events'

        if AllCategories[user] == 'Fitness':
            category = 'People & Blogs'

        if AllCategories[user] == 'DIY & Life Hacks':
            category = 'Howto & Style'

        YouTube_Channels.objects.create(url=f'https://www.youtube.com/channel/{finalURL}', category=category, location='Hong Kong')

    return HttpResponse('Done')