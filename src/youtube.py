from googleapiclient.discovery import build

import json

with open('credentials.json') as f:
    contents = json.load(f)
    youtube_key = contents['youtube_key']

def getYoutubeKey():
    return youtube_key

def getTrack(trackName, youtube_access_token):
    youtube = build('youtube', 'v3', developerKey=youtube_access_token)
    request = youtube.search().list(part='id', type='video', q=trackName, maxResults=1)
    response = request.execute()

    return response