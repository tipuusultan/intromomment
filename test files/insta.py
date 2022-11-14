# THIS SCRIPT TO GET INFORMATION FROM PARTICUAR INSTAGRAM ACCOUNT

# import instaloader
# import re
# # Creating an instance of Instaloader class
# bot = instaloader.Instaloader()
# profile = instaloader.Profile.from_username(bot.context, "krepoint")
# print("Username: ", profile.username)
# print("Bio: ", profile.biography)
# print("followers: ", profile.followers)
# print("Follwoings: ", profile.followees)
# print("Posts: ", profile.business_category_name)
# emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
# print("Emails extracted from the bio:")
# print(emails)
import requests
import urllib.request
import urllib.parse
import urllib.error
from bs4 import BeautifulSoup
import ssl
import json

class insta_Scraper_v1:

    def getinfo (self, url):
        html = urllib.request.urlopen('www.instagram.com/nbamemes', context=self.ctx).read()
        soup = BeautifulSoup(html, 'html.parser')
        data = soup.find_all ('meta', attr={'property': 'og:description'})

        text = data[0]
        user = '%s %s %s' % (test[-3], text[-2], text[-1])
        followers = text[0]
        following = text[2]
        posts = text[4]
        print ('User:', user)
        print ( 'Followers:', followers)
        print ('Following:', following)
        print ('Posts:', posts)
        print ('-----------------------')

    def mail(self):
        self.ctx = ssl.create_default_context()
        self.ctx.check_hostname = False
        self.ctx.verify_mode = ssl.CERT_NONE

    with open('123.txt') as f: 
        self.content = f.readlines()
        self.content = [x.strip() for x in self.content]
        for url in self.content:
            self.getinfo(url)

if __name__ == '__main__':
    obj = insta_Scraper_v1()
    obj.main()