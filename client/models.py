from django.db import models
from account.models import accounts
# Create your models here.



class client_profile(models.Model):
    user            = models.ForeignKey(accounts, on_delete=models.CASCADE)
    name            = models.CharField(max_length=100)
    url             = models.URLField(max_length=200)
    description     = models.TextField()
    #categories 

    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Client Profiles"
        verbose_name        = "Client Profiles"    





class categories(models.Model):
    name            = models.CharField(max_length=100)
    created_at      = models.DateTimeField(auto_now_add=True)
    updated_at      = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

    class Meta:
        verbose_name_plural = "Categories"
        verbose_name        = "Categories"


advertisement_format=(('post','Post'),('photo','Photo'),('video','Video'),('other','Other'))
platform_types = (('youtube','Youtube'),('facebook','Facebook'),('instagram','Instagram'))

class client_enquery(models.Model):
    id              = models.AutoField(primary_key=True)
    name            = models.CharField(max_length=100)
    email           = models.EmailField(max_length=100)
    telephone       = models.CharField(max_length=100)
    industry        = models.CharField(max_length=100)
    start_date      = models.DateField(help_text="Start Date of Advertising Period")
    end_date        = models.DateField(help_text="End Date of Advertising Period")
    adv_format      = models.CharField(max_length=30 , choices=advertisement_format, default='other') 
    categories      = models.CharField(max_length=50, blank=True, null=True)
    platform        = models.CharField(max_length=30 , choices=platform_types, default='other')
    followers       = models.CharField(max_length=300)

    created_at = models.DateTimeField(auto_now_add=True, blank=True, null=True)
    updated_at = models.DateTimeField(auto_now=True, blank=True, null=True)


    class Meta:
        verbose_name_plural = "Client Enqueries"
        verbose_name        = "Client Enqueries"
        











