# way 2
# from bs4 import BeautifulSoup
# import requests
# API = 'AIzaSyBVJd3jVKQ4qkqGxOQ0y84NDFKBsz_lDkY'
# url = f'https://www.googleapis.com/youtube/v3/search?part=snippet&q=gameplay&regionCode=HK&type=video&videoCategoryId=10&key={API}'
# r =requests.get(url)
# print(r.text)

# Way 1
# from youtubesearchpython import VideosSearch
# AllResult = []
# data = VideosSearch('游戏玩法', limit=51)
# AllResult.append(data.result()['result'])
# data.next()
# AllResult.append(data.result()['result'])
# data.next()
# AllResult.append(data.result()['result'])

# Videos = []
# for result in AllResult:
    
#     for r in result:
#         VideoURL = r['link']
#         Videos.append(VideoURL)
#         print(VideoURL)

# # function to find duplicate in a list
# def list_duplicates(seq):
#   seen = set()
#   seen_add = seen.add
#   # adds all elements it doesn't know yet to seen and all other to seen_twice
#   seen_twice = set( x for x in seq if x in seen or seen_add(x) )
#   # turn the set into a list (as requested)
#   return list( seen_twice )
# print(list_duplicates(Videos))
# print(len(Videos))


# way 3
# import requests
# from requests_html import HTMLSession

# from bs4 import BeautifulSoup
# from termcolor import colored
# import locale

# ChannelCrawlerCategories = {'Education':'876973', 'Entertainment':'980862', 'Film and Animation':'982376','Gaming':'964607','Howto & Style':'982377','Music':'982379', 'News & Politics':'982381','People & Blogs':'966857','Pets & Animals':'982385', 'Science & Technology':'928708', 'Sports':'344310','Travel & Events':'982386'}

# InputCategory = str(input('Enter Channel Category: '))

# Category = ChannelCrawlerCategories.get(InputCategory)
# print(colored('Searching Channels for ', 'red'), colored(InputCategory, 'green'),colored('.........'))

# from requests_html import HTMLSession
# url = f'https://channelcrawler.com/eng/results2/{Category}/'
# print(url)
# s = HTMLSession()
# r = s.get(url)
# r.html.render()

# html = BeautifulSoup(r.text, 'html.parser')

# import time

# time.sleep(10)
# TotalResult = html.select('.count-results')
# print(TotalResult)
# locale.setlocale( locale.LC_ALL, 'en_US.UTF-8' ) 
# locale.atoi(TotalResult)
# TotalPages = TotalResult/20
# print(TotalPages)

# AllChannels = []
# AllChannelsLinks = []
# for i in range(1, int(LastPage)+1):
#     new_r= requests.get(f'https://channelcrawler.com/eng/results2/{Category}/page:{i}')
#     new_html = BeautifulSoup(new_r.text, 'html.parser')
#     channels = new_html.select('.channel')
#     for channel in channels:
#         title = channel.select('a')[0].get_text()
#         link = channel.select('a')[0]['href']
#         AllChannels.append(title)
#         AllChannelsLinks.append(link)
#         print(colored(f'{len(AllChannels)} results found','red'))

# print(AllChannels)
# print(AllChannelsLinks)


# from youtubesearchpython import VideosSearch, ChannelsSearch
# AllResult = []
# data = ChannelsSearch('gaming', region='HK', language='zh-hk')
# AllResult.append(data.result()['result'])
# data.next()
# AllResult.append(data.result()['result'])
# data.next()
# AllResult.append(data.result()['result'])

# print(AllResult)
# Videos = []
# for result in AllResult:
    
#     for r in result:
#         VideoURL = r['link']
#         Videos.append(VideoURL)
#         print(VideoURL)

# # function to find duplicate in a list
# def list_duplicates(seq):
#   seen = set()
#   seen_add = seen.add
#   # adds all elements it doesn't know yet to seen and all other to seen_twice
#   seen_twice = set( x for x in seq if x in seen or seen_add(x) )
#   # turn the set into a list (as requested)
#   return list( seen_twice )
# print(list_duplicates(Videos))
# print(len(Videos))

# from youtubesearchpython import VideosSearch

# videosSearch = VideosSearch('NoCopyrightSounds', limit = 2)

# print(videosSearch.result())
# import urllib.request

from selenium import webdriver
import json, time
import translators as ts


def get_video_results():
    option = webdriver.ChromeOptions()
    option.add_argument('headless')
    driver = webdriver.Chrome("C:/chromedriver.exe",options=option)
    category=input("Enter Category: ")
    tc=ts.google(category, from_language='en', to_language='zh')
    print(tc)
    driver.get('https://www.youtube.com/results?search_query=hong+kong'+tc+"hong+kong")

    youtube_data = []

    # scrolling to the end of the page
    # https://stackoverflow.com/a/57076690/15164646
    # while True:
    #     # end_result = "No more results" string at the bottom of the page
    #     # this will be used to break out of the while loop
    #     end_result = driver.find_element("css selector", '#message').is_displayed()
    #     driver.execute_script("var scrollingElement = (document.scrollingElement || document.body);scrollingElement.scrollTop = scrollingElement.scrollHeight;")
    #     # time.sleep(1) # could be removed
    #     #print(end_result)

    #     # once element is located, break out of the loop
    #     if end_result == True:
    #         break
    # print('Extracting results. It might take a while...')
    links=[]
    for result in driver.find_elements("css selector", '.text-wrapper.style-scope.ytd-video-renderer'):
        title = result.find_element("css selector", '.title-and-badge.style-scope.ytd-video-renderer').text
        link = result.find_element("css selector", '.title-and-badge.style-scope.ytd-video-renderer a').get_attribute('href')
        channel_name = result.find_element("css selector", '.long-byline').text
        channel_link = result.find_element("css selector", '#text > a').get_attribute('href')
        #views = result.find_element("css selector", '.style-scope ytd-video-meta-block').text.split('\n')[0]
        #print(channel_link)
        option = webdriver.ChromeOptions()
        option.add_argument('headless')
        driver1 = webdriver.Chrome("C:/chromedriver.exe",options=option)
        driver1.get(channel_link+"/about")
        location=driver1.find_element('xpath','//*[@id="details-container"]/table/tbody/tr[2]/td[2]/yt-formatted-string').text
        if location=="Hong Kong":
            links.append(channel_link)
        

    #    # youtube_data.append({
    #         'title': title,
    #         'link': link,
    #         'channel': {'channel_name': channel_name, 'channel_link': channel_link},
            
    #    #})

    #print(json.dumps(youtube_data, indent=2, ensure_ascii=False))
    for i in links:
        print(i)
    driver.quit()

get_video_results()

