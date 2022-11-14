from django.contrib import admin
from .models import influencer_profile, YouTube_Channels,Facebook_Page, Instagram_Page, MostSubscribedYTChannel, MostViewedYTChannel, MostFollowedInstaPages
# Register your models here.

admin.site.register(influencer_profile)
class InfluencerProfileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "created_at",
        "updated_at",
    )


@admin.register(YouTube_Channels)
# admin.site.register(YouTube_Channels)
class YouTubeProfileAdmin(admin.ModelAdmin):
    list_display = (

        "name",
        "category",
        "Subs",
        "location"
    )
    list_filter = ( "category","location",)
    list_max_show_all = 1200
    list_per_page = 1000


@admin.register(Facebook_Page)
# admin.site.register(YouTube_Channels)
class FacebookProfileAdmin(admin.ModelAdmin):
    list_display = (
        "url",
        "category",
        "location"
    )
    list_filter = ( "category","location",)


@admin.register(Instagram_Page)
class InstagramProfileAdmin(admin.ModelAdmin):
    list_display = (
        "url",
        "category",
        "location"
    )
    list_filter = ( "category","location",)
    list_max_show_all = 1200
    list_per_page = 1000


@admin.register(MostSubscribedYTChannel)
class MostSubscribedYTChannel(admin.ModelAdmin):
    list_display = (
        "url",
        "subs",
        "TotalViews"
    )


@admin.register(MostViewedYTChannel)
class MostViewedYTChannel(admin.ModelAdmin):
    list_display = (
        "url",
        "subs",
        "TotalViews"
    )

@admin.register(MostFollowedInstaPages)
class MostFollowedInstaPages(admin.ModelAdmin):
    list_display = (
        "username",
        "followers",
        "posts"
    )
