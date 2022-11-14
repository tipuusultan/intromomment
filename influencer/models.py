from django.db import models
from account.models import accounts
# Create your models here.



class influencer_profile(models.Model):
    user                = models.ForeignKey(accounts, on_delete=models.CASCADE)
    name                = models.CharField(max_length=100)
    url                 = models.URLField(max_length=200 , null=True , blank=True)
    description         = models.TextField(null=True , blank=True)
    phone               = models.CharField(max_length=20 , null=True , blank=True)
    account_name_id     = models.CharField(max_length=100 , null=True , blank=True)

    Instagram_page_url = models.URLField(blank=True, max_length=2000, null=True)
    Instagram_page_category = models.CharField(blank=True, max_length=2000, null=True)

    Facebook_page_url = models.URLField(blank=True, max_length=2000, null=True)
    Facebook_page_category = models.CharField(blank=True, max_length=2000, null=True)

    Youtube_channel_url = models.URLField(blank=True, max_length=2000, null=True)
    Youtube_channel_category = models.CharField(blank=True, max_length=2000, null=True)

    Verified = models.BooleanField(default=False, blank=True, null=True)
    #categories      

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


    class Meta:
        verbose_name_plural = "Influencer Profiles"
        verbose_name        = "Influencer Profiles"


class YouTube_Channels(models.Model):
    id                  = models.AutoField(primary_key=True)
    user =              models.ForeignKey(accounts, on_delete=models.CASCADE, blank=True, null=True)
    url                 = models.URLField(max_length=2000 , null=True , blank=True)
    category            = models.CharField(max_length=200, blank=True, null=True)
    name            = models.CharField(max_length=200, blank=True, null=True)
    Subs                = models.CharField(max_length=12323232323 , blank=True, null=True)
    location            = models.CharField(max_length=200, null=True , blank=True )
    NumberofVideos      = models.IntegerField(blank=True, null=True)
    ProfilePicLink      = models.URLField(max_length=2000 , blank=True, null=True)
    AllVideos           = models.TextField(blank=True, null=True)
    def __str__(self):
        return self.url

class Instagram_Page(models.Model):
    id                  = models.AutoField(primary_key=True)
    user =              models.ForeignKey(accounts, on_delete=models.CASCADE, blank=True, null=True)
    name                = models.CharField(max_length=200, blank=True, null=True)
    url                 = models.URLField(max_length=2000 , null=True , blank=True)
    posts               = models.TextField(blank=True, null=True)
    postsCount               = models.CharField(max_length=50000000000000000000,blank=True, null=True)
    followersCount                = models.CharField(max_length=12323232323 , blank=True, null=True)
    ProfilePicLink      = models.URLField(max_length=20000 , blank=True, null=True)
    category            = models.CharField(max_length=200, blank=True, null=True)
    location            = models.CharField(max_length=200, null=True , blank=True )

    def __str__(self):
        return self.url

class Facebook_Page(models.Model):
    id                  = models.AutoField(primary_key=True)
    user =              models.ForeignKey(accounts, on_delete=models.CASCADE, blank=True, null=True)
    name            = models.CharField(max_length=200, blank=True, null=True)
    url                 = models.URLField(max_length=2000 , null=True , blank=True)
    posts               = models.TextField(blank=True, null=True)
    postsCount               = models.CharField(max_length=50000000000000000000,blank=True, null=True)
    followersCount                = models.CharField(max_length=12323232323 , blank=True, null=True)
    ProfilePicLink      = models.URLField(max_length=20000 , blank=True, null=True)
    category            = models.CharField(max_length=200, blank=True, null=True)
    location            = models.CharField(max_length=200, null=True , blank=True )

    def __str__(self):
        return self.url

class MostSubscribedYTChannel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=200, null=True , blank=True)
    uploads = models.CharField(max_length=200, blank=True, null=True)
    subs = models.CharField(max_length=200, blank=True, null=True)
    TotalViews = models.CharField(max_length=2020, blank=True, null=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

class MostViewedYTChannel(models.Model):
    name = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=200, null=True , blank=True)
    uploads = models.CharField(max_length=200, blank=True, null=True)
    subs = models.CharField(max_length=200, blank=True, null=True)
    TotalViews = models.CharField(max_length=2020, blank=True, null=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)
    
class MostFollowedInstaPages(models.Model):
    username = models.CharField(max_length=200, blank=True, null=True)
    url = models.URLField(max_length=200, null=True , blank=True)
    posts = models.CharField(max_length=200, blank=True, null=True)
    followers = models.CharField(max_length=200, blank=True, null=True)
    engagementRate = models.CharField(max_length=2020, blank=True, null=True)

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)