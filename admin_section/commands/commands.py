from django.shortcuts import render , redirect
from django.http import HttpResponse , JsonResponse
from account.models import accounts
from ..models import *
import random
from django.contrib import messages
from django.contrib.auth import authenticate,logout as deauth, login  as dj_login
from django.conf import settings 
from django.core.mail import send_mail

from influencer.models import *
from ..functions import GetTop20YTChannels, GetTop20InstaPages
# Create your views here.

def SaveTop20YT(request,id):

    Top20 = GetTop20YTChannels(condition=id)
    for top in Top20:
        username = top.get('Username')
        Subscribers = top.get('Subscribers')
        Uploads = top.get('Uploads')
        VideoViews = top.get('Video Views')
        Link = top.get('Link').split('/')[-1]
        URL = f'https://youtube.com/channel/{Link}'
        if id == 'mostsubscribed':
            MostSubscribedYTChannel.objects.create(name=username, subs=Subscribers,uploads=Uploads, url=URL, TotalViews=VideoViews)

        elif id == 'MostViewedYTChannel':
            MostViewedYTChannel.objects.create(name=username, subs=Subscribers,uploads=Uploads, url=URL, TotalViews=VideoViews)
    return HttpResponse('All data saved')

def SaveTop20Insta(request):

    Top20Insta = GetTop20InstaPages()
    for top in Top20Insta:
        username = top.get('Channel Info')
        posts = top.get('Posts')
        EngagementRate = top.get('Engagement Rate')
        Followers = top.get('Followers')
        Link = top.get('Link').split('/')[-1]
        URL = f'https://www.instagram.com/{Link}'
        MostFollowedInstaPages.objects.create(username=username, posts=posts,engagementRate=EngagementRate, url=URL, followers=Followers)

    return HttpResponse('All data saved')

from ..functions import GetSubscribersCount

def URLtoDataYT(request):
    from ..ChannelData import YTData
    from pytube import Channel, YouTube
    import pafy
    from datetime import datetime
    import time
    from ..functions import SeliniumInit, GetAllVideos_From_YTChannel_Selenium
    datas = YouTube_Channels.objects.all()
    
    driver = SeliniumInit()

    for d in datas:
        if d.AllVideos:
        # if d.name is None:
            # try:
            id = d.id
            c = Channel(d.url)
            Username = c.channel_id
            y = YTData(c.channel_id)

            # subscriberCount = GetSubscribersCount(d.url)
            # ChannelName = c.channel_name
            # TotalVideos = len(c.video_urls)
            # ProfilePicLink = y.ThumnailURL()
            AllVideosLinks = GetAllVideos_From_YTChannel_Selenium(ids=[c.channel_id],driver=driver, time=time)
            AllVideosData = []
            #fetch video details
            # for video in GetAllVideos_From_YTChannel_Selenium(ids=[c.channel_id],driver=driver, time=time):
            #     yt = YouTube(video)
            #     yt_pafy = pafy.new(video)
            #     publishDate = datetime.strptime(str(yt.publish_date), "%Y-%m-%d %H:%M:%S").strftime('%d-%m-%Y')
            #     AllVideosData.append({'title':yt.title,'views':yt.views, 'plub_date':publishDate , 'url':video,'likes':yt_pafy.likes})
            # print('Okay')
            # YTchannel.AllVideos = AllVideosData
            # # YTchannel.name = ChannelName
            # # YTchannel.Subs = subscriberCount
            # # YTchannel.ProfilePicLink = ProfilePicLink
            YTchannel = YouTube_Channels.objects.get(id=id)
            YTchannel.AllVideos = AllVideosLinks
            YTchannel.NumberofVideos = len(AllVideosLinks)
            YTchannel.save()
            print(AllVideosLinks)
            print('Data Saves')
            # except:
            #     print('something is wrong')
        else:
            print('Datas Available')

    return HttpResponse('okay')

def StoreFBPages(request):
    from selenium import webdriver
    from time import sleep
    from selenium.webdriver.chrome.options import Options
    from selenium.webdriver.common.by import By
    from selenium.webdriver.common.keys import Keys
    from selenium.webdriver.support.ui import WebDriverWait
    from selenium.webdriver.support import expected_conditions as EC


    i=0

    usr="intromomenthk@gmail.com"
    pwd="Qtdata1871"
    options = webdriver.ChromeOptions()
    options.add_argument('--ignore-certificate-errors')
    options.add_argument('--incognito')
    options.add_argument("--start-maximized")
    # options.add_argument('--headless')
    options.add_experimental_option( "prefs", {'protocol_handler.excluded_schemes.tel': False})
    driver = webdriver.Chrome("C:/chromedriver.exe",chrome_options=options)
    driver.get('https://www.facebook.com/')
    sleep(1)

    username_box = driver.find_element(By.XPATH,'//*[@id="email"]') 
    username_box.send_keys(usr)

    sleep(1)

    password_box = driver.find_element(By.XPATH,'//*[@id="pass"]')
    password_box.send_keys(pwd)

    login_box = driver.find_element('xpath','/html/body/div[1]/div[1]/div[1]/div/div/div/div[2]/div/div[1]/form/div[2]/button')
    login_box.click()
    sleep(5)

    AllPages=[]
    keywords = {
        'Gaming':['gaming', 'gameplay', 'gamer','gameplay video','pubg'],
        'Public Figure / Model / Actor':['actor', 'Public Figure','Model'],
        'Art':['Art'],
        'Musician/band':['Musician/band'],
        'Politician':['Politician'],
        'Producer':['Producer'],
        'Photographer':['Photographer'],
        'Dancer':['Dancer', 'dancing'],
        'Web designer':['Web designer'],
        'Education':['The instructor','Education'],
        'Editor/Journalist':['Journalist','Editor'],
        'Concert tour':['Concert tour'],
        'Motivational speaker':['Motivational speaker'],
    }

    GamingChannels = []
    PublicFigureModelctorChannels = []
    ArtChannels = []
    MusicianbandChannels = []
    PoliticianChannels = []
    ProducerChannels = []
    PhotographerChannels = []
    DancerChannels = []
    WebDsignerChannels = []
    EducationChannels = []
    EitorJournalistChannels = []
    ConcerTourChannels = []
    MotivationalSpeakerChannels = []


    for keyword in keywords:
        for search in keywords.get(keyword):
            driver.get(f"https://www.facebook.com/search/pages?q={search}&filters=eyJmaWx0ZXJfcGFnZXNfbG9jYXRpb246MCI6IntcIm5hbWVcIjpcImZpbHRlcl9wYWdlc19sb2NhdGlvblwiLFwiYXJnc1wiOlwiMTEzMzE3NjA1MzQ1NzUxXCJ9IiwiY2F0ZWdvcnk6MCI6IntcIm5hbWVcIjpcInBhZ2VzX2NhdGVnb3J5XCIsXCJhcmdzXCI6XCIxMDA3LDE4MDE2NDY0ODY4NTk4MlwifSJ9")
            sleep(5)
            for j in range(0,10):
                driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")
                sleep(3)
            ContentBox = driver.find_elements_by_class_name('x1yztbdb')
            try:
                for t in ContentBox:
                    a = t.find_elements_by_tag_name('a')
                    for i in a:
                        if i.text == '':
                            pass
                        else:
                            AllPages.append({'Name': i.text ,'URL': i.get_attribute('href') , 'Category':keyword})
            except:
                print("SOMETHING WRONG")

    for page in AllPages:
        Name = page.get('Name')       
        URL = page.get('URL')       
        Category = page.get('Category')       
        Location = 'Hong Kong'   

        Facebook_Page.objects.create(name=Name, url=URL, category=Category, location=Location)
        print('Data Stored')
    return HttpResponse('Done')