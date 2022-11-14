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
import requests
from bs4 import BeautifulSoup
from termcolor import colored

ChannelCrawlerCategories = {'Education':'876973', 'Entertainment':'980862', 'Film and Animation':'982376','Gaming':'964607','Howto & Style':'982377','Music':'982379', 'News & Politics':'982381','People & Blogs':'966857','Pets & Animals':'982385', 'Science & Technology':'928708', 'Sports':'344310','Travel & Events':'982386'}

InputCategory = str(input('Enter Channel Category: '))

Category = ChannelCrawlerCategories.get(InputCategory)
print(colored('Searching Channels for ', 'red'), colored(InputCategory, 'green'),colored('.........'))

r= requests.get(f'https://channelcrawler.com/eng/results2/{Category}/')
html = BeautifulSoup(r.text, 'html.parser')
pagination = html.select('.pagination')

for p in pagination:
    LastPage = p.select('a')[-2].get_text()

AllChannels = []
AllChannelsLinks = []
for i in range(1, int(LastPage)+1):
    new_r= requests.get(f'https://channelcrawler.com/eng/results2/{Category}/page:{i}')
    new_html = BeautifulSoup(new_r.text, 'html.parser')
    channels = new_html.select('.channel')
    for channel in channels:
        title = channel.select('a')[0].get_text()
        link = channel.select('a')[0]['href']
        AllChannels.append(title)
        AllChannelsLinks.append(link)
        print(colored(f'{len(AllChannels)} results found','red'))

print(AllChannels)
print(AllChannelsLinks)
