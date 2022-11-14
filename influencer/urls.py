from django.urls import path
from influencer.views import *


app_name = 'influencer'


urlpatterns = [ 
    path('influencer-register/' , influencer_register , name="influencer-register" ) ,
    path('influencer-register-step2' , influencer_register_step2 , name="influencer-register-step2" ) ,
    path('check-email' , check_email , name="check-email" ) ,
    path('check-otp/' , check_otp , name="check-otp" ) ,
    path('login/' , login , name="login" ) ,
    path('logout', logout, name="logout"),
    path('add_youtube/', add_youtube, name="add_youtube"),
    path('profile-settings/', ProfileSettings, name="ProfileSettings"),
    path('store/', StoreInfluencer, name="StoreInfluencer"),
]
