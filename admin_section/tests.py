from django.test import TestCase

# Create your tests here.
# from pytube import Channel
# import instaloader
# import re
# # Creating an instance of Instaloader class
# bot = instaloader.Instaloader()
# profile = instaloader.Profile.from_username(bot.context, "https://www.instagram.com/viutv")
# print("Username: ", profile.username)
# print("Bio: ", profile.biography)
# print("followers: ", profile.followers)
# print("Follwoings: ", profile.followees)
# print("Posts: ", profile.business_category_name)
# emails = re.findall(r"\b[A-Za-z0-9._%+-]+@[A-Za-z0-9.-]+\.[A-Z|a-z]{2,}\b", profile.biography)
# print("Emails extracted from the bio:")
# print(emails)
# import httpx


# def find_location_id(query: str, session: httpx.Client):
#     """finds most likely location ID from given location name"""
#     resp = session.get(f"https://www.instagram.com/web/search/topsearch/?query={query}")
#     data = resp.json()
#     try:
#         first_result = sorted(data["places"], key=lambda place: place["position"])[0]
#         return first_result["place"]["location"]["pk"]
#     except IndexError:
#         print(f'no locations matching query "{query}" were found')
#         return


# def scrape_users_by_location(location_id: str, session: httpx.Client, page_limit=None):
#     url = f"https://www.instagram.com/explore/locations/{location_id}/?__a=1"
#     page = 1
#     next_id = ""
#     while True:
#         resp = session.get(url + (f"&max_id={next_id}" if next_id else ""))
#         data = resp.json()["native_location_data"]
#         print(f"scraped location {location_id} page {page}")
#         for section in data["recent"]["sections"]:
#             for media in section["layout_content"]["medias"]:
#                 yield media["media"]["user"]["username"]
#         next_id = data["recent"]["next_max_id"]
#         if not next_id:
#             print(f"no more results after page {page}")
#             break
#         if page_limit and page_limit < page:
#             print(f"reached page limit {page}")
#             break
#         page += 1


# if __name__ == "__main__":
#     with httpx.Client(
#         timeout=httpx.Timeout(20.0)
#     ) as session:
#         location_name = "india"
#         location_id = find_location_id(location_name, session=session)
#         print(f'resolved location id from {location_name} to {location_id}')
#         for username in scrape_users_by_location(location_id, session=session):
#             print(username)

# from instascrape import *
# # url = 'https://www.instagram.com/explore/locations/214424288/hong-kong/'
# # new_york = Location(url)
# # new_york.scrape()

# # recent_posts = new_york.get_recent_posts()
# # print(recent_posts)
# # for post in recent_posts:
# #     print(post.upload_date)
# from instascrape import Profile 
# profile = Profile('chris_greening')
# profile.scrape()


def Top10YTChannels():
    from selenium import webdriver
    web = webdriver.Chrome('C:/chromedriver.exe')
    web.get('https://socialblade.com/youtube/top/country/hk/mostsubscribed')
    data = web.find_elements_by_xpath('/html/body/div[11]/div[2]/div[5]/div[3]/a')
    print(data.text)
    
from selenium import webdriver
import json, time


def get_video_results():
    driver = webdriver.Chrome('C:/chromedriver.exe')
    driver.get('https://www.youtube.com/results?search_query=minecraft')

    youtube_data = []

    # scrolling to the end of the page
    # https://stackoverflow.com/a/57076690/15164646
    while True:
        # end_result = "No more results" string at the bottom of the page
        # this will be used to break out of the while loop
        end_result = driver.find_element_by_css_selector('#message').is_displayed()
        driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
        # time.sleep(1) # could be removed
        print(end_result)

        # once element is located, break out of the loop
        if end_result == True:
            break

    print('Extracting results. It might take a while...')

    for result in driver.find_elements_by_css_selector('.text-wrapper.style-scope.ytd-video-renderer'):
        title = result.find_element_by_css_selector('.title-and-badge.style-scope.ytd-video-renderer').text
        link = result.find_element_by_css_selector('.title-and-badge.style-scope.ytd-video-renderer a').get_attribute('href')
        channel_name = result.find_element_by_css_selector('.long-byline').text
        channel_link = result.find_element_by_css_selector('#text > a').get_attribute('href')
        views = result.find_element_by_css_selector('.style-scope ytd-video-meta-block').text.split('\n')[0]

        try:
            time_published = result.find_element_by_css_selector('.style-scope ytd-video-meta-block').text.split('\n')[1]
        except:
            time_published = None

        try:
            snippet = result.find_element_by_css_selector('.metadata-snippet-container').text
        except:
            snippet = None

        try:
            if result.find_element_by_css_selector('#channel-name .ytd-badge-supported-renderer') is not None:
                verified_badge = True
            else:
                verified_badge = False
        except:
            verified_badge = None

        try:
            extensions = result.find_element_by_css_selector('#badges .ytd-badge-supported-renderer').text
        except:
            extensions = None
        print(verified_badge)

        youtube_data.append({
            'title': title,
            'link': link,
            'channel': {'channel_name': channel_name, 'channel_link': channel_link},
            'views': views,
            'time_published': time_published,
            'snippet': snippet,
            'verified_badge': verified_badge,
            'extensions': extensions,
        })

    print(json.dumps(youtube_data, indent=2, ensure_ascii=False))

    driver.quit()



# part of the output:
'''
[
  {
    "title": "I Survived 100 Days in Ancient Greece on Minecraft.. Here's What Happened..",
    "link": "https://www.youtube.com/watch?v=hUAjdnhpTXU",
    "channel": {
      "channel_name": "Forrestbono",
      "channel_link": "https://www.youtube.com/user/ForrestboneMC"
    },
    "views": "2.6M views",
    "time_published": "5 days ago",
    "snippet": "I had to survive for 100 Days of Hardcore Minecraft in Ancient Greece and battle Poseidon, God of the Sea, and Cronos, the God ...",
    "verified_badge": true,
    "extensions": "New"
  }
]
'''



# # PYTHON MODULES TO USE
# from selenium import webdriver as selenium_webdriver
# from selenium.webdriver.firefox.options import Options as selenium_options
# from selenium.webdriver.common.desired_capabilities import DesiredCapabilities as selenium_DesiredCapabilities

# # FIRE UP A HEADLESS BROWSER SESSION WITH A "SCREEN SIZE" OF 1920x1080

# browser_options = selenium_options()
# browser_options.add_argument("--headless")
# browser_options.add_argument("--window-size=1920,1080")

# capabilities_argument = selenium_DesiredCapabilities().FIREFOX
# capabilities_argument["marionette"] = True

# browser = selenium_webdriver.Chrome('C:/chromedriver.exe')

# import time
# browser.set_window_size(800, 800)
# browser.get("https://www.youtube.com/channel/UC9Ije5dQVFx9uTGddG_U5XA/videos")
# print(browser.current_url)

# browser.save_screenshot("screenshot.png")
# from IPython.display import Image
# Image("screenshot.png", width=800, height=800)

from pytube import Channel
import json

class YTData:
    def __init__(self,ChannelID):
        print('YTData Module')
        self.YT_API = 'AIzaSyArAj0JJdaetxKRJokWujiabzrmJ2jFZI8'
        # self.ChannelID = 'UCCW2r95gBpDm7DqEtiFKOlQ'
        self.url = f'https://www.googleapis.com/youtube/v3/channels?part=brandingSettings,contentDetails,contentOwnerDetails,id,localizations,snippet,statistics,status,topicDetails&id={ChannelID}&key={self.YT_API}'
        self.r = requests.get(self.url)
        self.data = self.r.text
        self.JsonData = json.loads(self.data)

    def ChannelName(self):
        return self.JsonData['items'][0]['snippet']['title']
    
    def SubsCount(self):
        return self.JsonData['items'][0]['statistics']['subscriberCount']

    def ThumnailURL(self):
        return self.JsonData['items'][0]['snippet']['thumbnails']['high']['url']

    def Location(self):
        return self.JsonData['items'][0]['snippet']['country']

from selenium import webdriver
from packaging import __version__
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.options import Options
opt = Options()
opt.headless = True
driver = webdriver.Chrome(ChromeDriverManager().install(),chrome_options=opt)
driver.get("https://www.noxinfluencer.com/instagram-channel-rank/top-100-hk-all-sorted-by-followers-weekly")
driver.implicitly_wait(20)
s = driver.find_elements("xpath", "//a[@class='link clearfix']")
b = driver.find_elements("xpath", "//div[@id='table-body']/div/span")
mlist = ["Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers","Channel Info", "Posts", "Engagement Rate", "Followers", "Channel Info", "Posts", "Engagement Rate", "Followers" ]
linkbox = []
totallist = []
count = 0
for i in b:
    totallist.append(i.text)
    count = count+1
    if count == 120:
        break
for i in totallist:
    if i == "":
        totallist.remove(i)
for i in range(0,80,4):
    totallist.pop(i)

file = list(zip(mlist, totallist))

c = 0
for i in s:
    linkbox.append(i.get_attribute("href"))
    c = c+1
    if c == 20:
        break
linkbox2=["Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link", "Link"]
file2 = list(zip(linkbox2, linkbox))



u1 = file[0],file[1],file[2],file[3],file2[0]
u2 = file[4],file[5],file[6],file[7],file2[1]
u3 = file[8],file[9],file[10],file[11],file2[2]
u4 = file[12],file[13],file[14],file[15],file2[3]
u5 = file[16],file[17],file[18],file[19],file2[4]
u6 = file[20],file[21],file[22],file[23],file2[5]
u7 = file[24],file[25],file[26],file[27],file2[6]
u8 = file[28],file[29],file[30],file[31],file2[7]
u9 = file[32],file[33],file[34],file[35],file2[8]
u10 = file[36],file[37],file[38],file[39],file2[9]
u11= file[40],file[41],file[42],file[43],file2[10]
u12= file[44],file[45],file[46],file[47],file2[11]
u13= file[48],file[49],file[50],file[51],file2[12]
u14= file[52],file[53],file[54],file[55],file2[13]
u15 = file[56],file[57],file[58],file[59],file2[14]
u16 = file[60],file[61],file[62],file[63],file2[15]
u17= file[64],file[65],file[66],file[67],file2[16]
u18= file[68],file[69],file[70],file[71],file2[17]
u19= file[72],file[73],file[74],file[75],file2[18]
u20= file[76],file[77],file[78],file[79],file2[19]
user1 = dict(u1)
user2 = dict(u2)
user3 = dict(u3)
user4 = dict(u4)
user5 = dict(u5)
user6 = dict(u6)
user7 = dict(u7)
user8 = dict(u8)
user9 = dict(u9)
user10 = dict(u10)
user11= dict(u11)
user12= dict(u12)
user13= dict(u13)
user14= dict(u14)
user15= dict(u15)
user16= dict(u16)
user17= dict(u17)
user18= dict(u18)
user19= dict(u19)
user20= dict(u20)
print(user1)
print(user2)
print(user3)
print(user4)
print(user5)
print(user6)
print(user7)
print(user8)
print(user9)
print(user10)
print(user11)
print(user12)
print(user13)
print(user14)
print(user15)
print(user16)
print(user17)
print(user18)
print(user19)
print(user20)


