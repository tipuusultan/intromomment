from django.test import TestCase


from scrape_instagram import *
response =instagram.profile_scraper(profile_link="https://www.instagram.com/celmirashop/")

print(response)