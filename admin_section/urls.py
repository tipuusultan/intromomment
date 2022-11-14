from django.urls import path
from .views import *
from .commands import commands

app_name = 'admin_section'


urlpatterns = [ 
   path('admin-login/' , admin_sign_in , name="admin-login")                  ,
   path('admin-logout/', admin_logout , name="admin-logout")                  ,
   path('admin-dashboard/', admin_dashoard , name="admin-dashboard" )         ,
   path('all-influencers/', All_Registered_Influencers , name="all_influencers" )         ,
   path('enquiry-view/' , admin_enquiry_view , name="admin_enquiry_view")     ,  
   path('see-influencers/<int:id>' , get_influencers , name="get_influencers")     ,  
   path('youtube-channel/<str:id>' , SingleChannel , name="single_channel")     ,  
   path('insta-page/<str:id>' , SinglePageInsta , name="single_page_insta")     ,  
   path('savetop20youtubers/<str:id>' , commands.SaveTop20YT , name="mostsubscribedytchannel")     ,  
   path('save-top20-insta/' , commands.SaveTop20Insta , name="saveTopInsta")     ,  
   path('save-yt/' , commands.URLtoDataYT , name="saveyt")     ,  
   path('save-fb/' , commands.StoreFBPages , name="savefb")     ,  

   path('fetch-details' , fetch_details , name="fetch-details"),
   path('get_data' , get_data , name="get_data"),
   path('challen-view/' , challen_view , name="challen-view"),
   path('get_video' , get_video, name="get_video")


]
