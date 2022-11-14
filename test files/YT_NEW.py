import requests
import json

YT_API = 'AIzaSyDFHQITXnQxqsbfaywe1yu3eHHhjo4Bfso'
url = f'https://www.googleapis.com/youtube/v3/search?key={YT_API}&channelId=UCrwP9T4wG4bG5QR_Vr1rXNA&part=snippet,id&order=date&maxResults=50'
r = requests.get(url)
data = r.text
JsonData = json.loads(data)
pageInfo = JsonData['pageInfo']['totalResults']

AllVideos = []

for i in range(0, (pageInfo-1)):    
    videoID = JsonData['items'][i]['id']['videoId']
    VidTitle = JsonData['items'][i]['snippet']['title']
    AllVideos.append({'Link':f'https://www.youtube.com/watch?v={videoID}' , 'Title': VidTitle})


import urllib
import json

def get_all_video_in_channel(channel_id='UCkh1LOz6bga3xuMf7MNxE-w'):
    api_key = 'AIzaSyDFHQITXnQxqsbfaywe1yu3eHHhjo4Bfso'

    base_video_url = 'https://www.youtube.com/watch?v='
    base_search_url = 'https://www.googleapis.com/youtube/v3/search?'

    first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(api_key, channel_id)

    video_links = []
    url = first_url
    while True:
        inp = urllib.request.urlopen(url)
        resp = json.load(inp)

        for i in resp['items']:
            if i['id']['kind'] == "youtube#video":
                video_links.append(base_video_url + i['id']['videoId'])

        try:
            next_page_token = resp['nextPageToken']
            url = first_url + '&pageToken={}'.format(next_page_token)
        except:
            break
    return video_links

import scrapetube

videos = scrapetube.get_search("python")

for video in videos:
    print(video['videoId'])