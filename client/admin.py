from django.contrib import admin
from .models import *
# Register your models here.

@admin.register(client_profile)
class client_profileAdmin(admin.ModelAdmin):
    list_display = (
        "user",
        "name",
        "url",
        "description",
        "created_at",
        "updated_at",
    )

admin.site.register(categories)

@admin.register(client_enquery)
class AdminClient(admin.ModelAdmin):
    list_display = (
        "name",
        "email",
        "telephone",
        "industry",
        "start_date",
        "end_date",
        "adv_format",
        "categories",
        "platform",
        "followers"
    )
    list_filter = ( "categories","platform",)
