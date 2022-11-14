import requests
import json
import urllib

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
    
    def AllVideo(self):
        pass



# though API 
# def get_all_video_in_channel(channelID='UCkh1LOz6bga3xuMf7MNxE-w'):
#     # YT_API = 'AIzaSyDFHQITXnQxqsbfaywe1yu3eHHhjo4Bfso'
#     # YT_API = 'AIzaSyA8FPm_nx16sWCDjEnUR2hZ8vV512f3mIM'
#     YT_API = 'AIzaSyCnim3noiXSL0xrf2a-ekEKP6_IBQKhjFQ'
#     base_video_url = 'https://www.youtube.com/watch?v='
#     base_search_url = 'https://www.googleapis.com/youtube/v3/search?'
#     first_url = base_search_url+'key={}&channelId={}&part=snippet,id&order=date&maxResults=25'.format(YT_API, channelID)

#     video_links = []
#     url = first_url
#     while True:
#         inp = urllib.request.urlopen(url)
#         resp = json.load(inp)

#         for i in resp['items']:
#             if i['id']['kind'] == "youtube#video":
#                 video_links.append(base_video_url + i['id']['videoId'])

#         try:
#             next_page_token = resp['nextPageToken']
#             url = first_url + '&pageToken={}'.format(next_page_token)
#         except:
#             break
#     return video_links

# Without API 
from youtubesearchpython import *
def get_all_video_in_channel(channelID='UCkh1LOz6bga3xuMf7MNxE-w'):
    playlist = Playlist(playlist_from_channel_id(channelID))
    video_links = playlist.videos

    while playlist.hasMoreVideos:
        playlist.getNextVideos()
        video_links = playlist.videos
    return video_links


def getVideoComments(videoID='cQZF8o4o6_Q'):
    comments = Comments(videoID)
    AllComments = comments.comments["result"]
    while comments.hasMoreComments:
        print('Getting more comments...')
        comments.getNextComments()
        AllComments = comments.comments["result"]
    return AllComments


