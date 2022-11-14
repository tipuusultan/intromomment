from django.contrib import admin
from .models import *

from django.contrib.auth.admin import UserAdmin




class UserAccountAdmin(UserAdmin):
    list_display=('email','username','date_joined')
    search_fields=('email','username')
    readonly_fields=('id','date_joined')

    filter_horizontal=()
    list_filter=()

admin.site.register(accounts ,UserAccountAdmin)    
