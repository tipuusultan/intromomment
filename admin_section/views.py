from email import message
from django.shortcuts import render , redirect
from django.contrib.auth import authenticate, logout ,login 
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import *
from influencer.models import YouTube_Channels, Facebook_Page, Instagram_Page, MostSubscribedYTChannel, MostViewedYTChannel, MostFollowedInstaPages
from django.http import  JsonResponse,HttpResponse

from client.models import *
from pytube import Channel
from .functions import GetSubscribersCount, ConvertStringNumberToNumber, GetTop20YTChannels,GetAllVideos_From_YTChannel_Selenium
import instaloader
from .ChannelData import YTData,get_all_video_in_channel, getVideoComments
from influencer.models import influencer_profile
# Create your views here.


def admin_sign_in(request):
    print("request is ",request.POST)   
    if request.user.is_authenticated: 
        return redirect("admin_section:admin-dashboard")
    if request.POST:
        form = AccountAuthenticationForm(request.POST)
        if form.is_valid():
            email = request.POST['email']
            password = request.POST['password']
            user = authenticate(email=email, password=password) 
            if user:
                if user.is_admin:
                    login(request, user)
                    return redirect("admin_section:admin-dashboard")
                else:
                    logout(request)
                    messages.info(request , "You have no access") 
                    return redirect('admin_section:admin-login')  

            else:
                messages.info(request , "Inalid Credentials") 
                return redirect('admin_section:admin-login')   
    return render(request , 'signIn/sign-in.html')



@login_required(login_url='admin_section:admin-login')
def admin_logout(request):
    logout(request)
    messages.info(request , 'You are Logout Successfully')
    return redirect('admin_section:admin-login') 



@login_required(login_url='admin_section:admin-login')
def admin_dashoard(request):
    # Top20 = GetTop20YTChannels()
    # print(Top20)
    # for top in Top20:
    #     username = top.get('Username')
    #     Subscribers = top.get('Subscribers')
    #     Uploads = top.get('Uploads')
    #     VideoViews = top.get('Video Views')
    #     Link = top.get('Link').split('/')[-1]
    #     URL = f'https://youtube.com/channel/{Link}'
    #     print(Link)
    #     MostSubscribedYTChannel.objects.create(name=username, subs=Subscribers,uploads=Uploads, url=URL, TotalViews=VideoViews)
    MostSubscribedchannels = MostSubscribedYTChannel.objects.all()
    MostViewedchannels = MostViewedYTChannel.objects.all()
    TopFollowedInstaPages = MostFollowedInstaPages.objects.all()
    context = {
        'MostSubscribedchannels':MostSubscribedchannels, 
        'MostViewedchannels':MostViewedchannels,
        'TopFollowedInstaPages':TopFollowedInstaPages
        }
    return render(request , 'dashboard/dashboard.html',context )


@login_required(login_url='admin_section:admin-login')
def admin_enquiry_view(request):
    enquiries = client_enquery.objects.all()
    print(enquiries)
    return render(request , 'dashboard/enquiry.html', {'enquiries':enquiries} )

def get_data(request):
    #fetching ifluencers for selected enquiry
    ids= request.POST.get('security_code')
    d = client_enquery.objects.filter(id=ids).first()
    id_list=[]
    if d.platform == 'youtube':
        Influencers = YouTube_Channels.objects.filter(category=d.categories)
        for i in Influencers:
            id_list.append({"id":i.id})
        return JsonResponse({"status":"success" , "data":id_list})  
    elif d.platform == 'instagram':
        Pages=[]
        Influencers = Instagram_Page.objects.filter(category=d.categories)
        for Influencer in Influencers:
            id_list.append({"id":Influencer.id})
        
        return JsonResponse({"status":"success" , "data":id_list}) 
    else:    
        return JsonResponse({"status":"failed" , "data":[]})   
    


@login_required(login_url='admin_section:admin-login')
def get_influencers(request, id):
    # fetching ifluencers for selected enquiry
    d = client_enquery.objects.filter(id=id).first()

    if d.platform == 'youtube':
        Influencers = YouTube_Channels.objects.filter(category=d.categories)
        
        return render(request , 'dashboard/influencers.html', {'influencers':Influencers ,'enquery_id':d.id } )
    else:
        Pages =[]
        return render(request , 'dashboard/influencers-insta.html',  {'enquery_id':d.id } )



def fetch_details(request):
    print(request.POST)
    ids= request.POST.get('security_code')
    rows_id = request.POST.get('rows_id')
    Channels = []
    if request.POST:
        d = client_enquery.objects.filter(id=ids).first()
        if d.platform == 'youtube':
            # filtering influencers for selected category
            Influencers = YouTube_Channels.objects.filter(category=d.categories , id=rows_id)
            for channel in Influencers:
                # fetching youtube channel subscribers
                print(channel.id)
                subsCount = channel.Subs
                print("subsCount", subsCount)
                # fetching client selected subscribers count
                SelectedSubscribersCount = d.followers
                ClientSelectSubscribersList = SelectedSubscribersCount.split(' to ')

                MinSubs = ConvertStringNumberToNumber(ClientSelectSubscribersList[0])
                MaxSubs = ConvertStringNumberToNumber(ClientSelectSubscribersList[1])

                if int(subsCount) > int(MinSubs) and int(subsCount) < int(MaxSubs):
                    c = Channel(str(channel))
                    ChannelName = channel.name
                    Username = c.channel_id
                    TotalVideos = len(get_all_video_in_channel(c.channel_id))
                    dt={                'ChannelName':ChannelName, 
                                        'TotalVideos':TotalVideos, 
                                        'URL'        :str(channel), 
                                        'Category'   :d.categories,
                                        'Username'   :Username ,
                                        'subscribe':subsCount
                                        }
                    Channels.append(dt)
                else:
                    pass

                print("channels details",Channels)
        else:
            Pages=[]
            from .functions import GetInstaPageDetails, SeliniumInit
            import re

            # uncomment below code when you use selenium scraping
            # driver = SeliniumInit()
            # cookiePath = r'C:\Users\Mr Sultan\Desktop\intromomment\admin_section\auth.pkl'

            Influencers = Instagram_Page.objects.filter(category=d.categories , id=rows_id)
            for Influencer in Influencers:
                username = Influencer.url.split('/')[-1]
                PageURL = f'https://www.instagram.com/{username}'

                # uncomment below code when you use selenium scraping
                # Number_of_Posts, Number_of_Followers = GetInstaPageDetails(username, cookiePath, driver)

                Number_of_Followers , Number_of_Posts= GetInstaPageDetails(username)

                # uncomment below code when you use selenium scraping
                # strFollowers = Number_of_Followers.split(' ')
                # followers = ConvertStringNumberToNumber(strFollowers[0])

                
                followers = ConvertStringNumberToNumber(Number_of_Followers)

                # fetching client selected followers count
                ClientSelectedFollowers = d.followers
                ClientSelectFollowersList = ClientSelectedFollowers.split(' to ')

                MinFollow = ConvertStringNumberToNumber(ClientSelectFollowersList[0])
                MaxFollow = ConvertStringNumberToNumber(ClientSelectFollowersList[1])

                if int(followers) > int(MinFollow) and int(followers) < int(MaxFollow):
                    TotalPosts = Number_of_Posts
                    Channels.append({'Username':username, 'TotalPosts':TotalPosts, 'URL':str(Influencer.url), 'Category':Influencer.category})

        data={
            'status': "success" ,
            'data': Channels
        }
        return  JsonResponse(data , safe=False)

@login_required(login_url='admin_section:admin-login')
def SingleChannel(request, id):
    context={
        "channel":id
    }
    return render(request , 'dashboard/single-channel-yt.html',context)

@login_required(login_url='admin_section:admin-login')
def challen_view(request):
    from pytube import Channel, YouTube
    import pafy
    import scrapetube
    from datetime import datetime
    ids=request.POST.get('security_code')
    c = Channel(f'https://www.youtube.com/channel/{ids}')
    y = YTData(ids)
    AllVideosList = get_all_video_in_channel(channelID=ids)
    AllVideosData = []
    context = {
        'ChannelURL': f'https://www.youtube.com/channel/{id}',
        'Name':y.ChannelName(),
        'SubsCount':y.SubsCount(),
        'ChannelLogo':y.ThumnailURL(),
        'ChannelLocation':y.Location(),
        # 'Videos':AllVideosData,
        'VideosCount':AllVideosList,
    }
    return JsonResponse(context)

def get_video(request):
    from pytube import Channel, YouTube
    import pafy
    import scrapetube
    from datetime import datetime

    rows_id=request.POST.get('rows_id')
    VideoLink = f"https://www.youtube.com/watch?v={rows_id}"
    # if 'youtube.com' in str(video):
    try:
        yt = YouTube(VideoLink)
        yt_pafy = pafy.new(VideoLink)
        publishDate = datetime.strptime(str(yt.publish_date), "%Y-%m-%d %H:%M:%S").strftime('%d-%m-%Y')
        try:
            CommentsCount = len(getVideoComments(rows_id))
        except:
            CommentsCount = 'No Comments'
        return JsonResponse(
                        {'title':yt.title,'views':yt.views, 'plub_date':publishDate , 'url':VideoLink,'likes':yt_pafy.likes,'CommentsCount':CommentsCount}
        )
        
    except:
        yt = YouTube(VideoLink)
        publishDate = datetime.strptime(str(yt.publish_date), "%Y-%m-%d %H:%M:%S").strftime('%d-%m-%Y')
        try:
            CommentsCount = len(getVideoComments(rows_id))
        except:
            CommentsCount = 'No Comments'
        return JsonResponse({'title':yt.title,'views':yt.views, 'plub_date':publishDate , 'url':VideoLink, 'likes':'Unble to fetch','CommentsCount':CommentsCount})


@login_required(login_url='admin_section:admin-login')
def SinglePageInsta(request, id):
    import instaloader

    bot = instaloader.Instaloader()

    profile = instaloader.Profile.from_username(bot.context, id)
    name = profile.full_name
    followers = profile.followers
    profilePIC = profile.get_profile_pic_url()
    Location = 'Hong Kong'
    url = f'https://www.instagram.com/{id}'
    PostsCount = profile.get_posts().count
    PostLinks = profile.get_posts()

    context = {
        'PageURL': url,
        'username':id,
        'FullName':name,
        'FollowersCount':followers,
        'profilepic':profilePIC,
        'Location':Location,
        'PostsCount':PostsCount,        
        'Posts':PostLinks,        
    }
    return render(request , 'dashboard/single-page-insta.html' ,context)


@login_required(login_url='admin_section:admin-login')
def All_Registered_Influencers(request):
    AllInfluencers = influencer_profile.objects.all()
    context = {
        'infleuncers':AllInfluencers,
    }
    return render(request, 'dashboard/All_Registered_Influencers.html',context) 
