from googleapiclient.discovery import build
from pytube import YouTube

import os
import re
from moviepy.editor import *
import requests 
import json 

URL = "https://accounts.spotify.com/api/token"
Base_URL = 'https://api.spotify.com/v1/'

YouTube_URL = 'https://www.youtube.com/watch?v='

playlist_link = input("Enter Spotify Playlist Link: ")
playlist_id = playlist_link[34:56]

# Get credentials for API
with open('credentials.json') as f:
    contents = json.load(f)

    Spotify_client_ID = contents['spotify_client_ID']
    Spotify_client_secret = contents['spotify_client_secret']
    youtube_key = contents['youtube_key']

# Get access token for spotify API
def getSpotifyAuth():
    res = requests.post(URL, {
    'grant_type': 'client_credentials',
    'client_id' : Spotify_client_ID,
    'client_secret' : Spotify_client_secret,
    })

    resData = res.json()
    accessToken = resData['access_token']
    return accessToken

TrackTitleList = []
VideoIDList = []

# Set headers to send Spotify Auth token
accessToken = getSpotifyAuth()
headers = {
    'Authorization' : 'Bearer {token}'.format(token=accessToken)
}

# Method to get track info 
def getTrackInfo(track_id, accessToken):
    r = requests.get(Base_URL + 'tracks/' + track_id, headers=headers)
    rJson = r.json()

    TrackName = rJson['name']
    Artist = rJson['artists'][0]['name']
    return Artist + ' - ' + TrackName

# We need a method to get a list of tracks in a playlist and extract the track ID. We will use this to get the artist and track name
def getPlaylist(playlist_id, accessToken):
    r = requests.get(Base_URL + 'playlists/' + playlist_id, headers=headers)
    rJson = r.json()
    total_tracks = rJson['tracks']['total']

    print("Total Tracks: ", total_tracks)
    print()

    ID_List = []
    
    for i in range(total_tracks):
        track_id = rJson['tracks']['items'][i]['track']['id']
        ID_List.append(track_id)

    for song in ID_List:
        trackName = getTrackInfo(song, accessToken)
        TrackTitleList.append(trackName)

        results = getTrack(trackName, youtube_key)

        trackID = results['items'][0]['id']['videoId']
        VideoIDList.append(trackID)

# Search Youtube for track name for use in getPlaylist
def getTrack(trackName, youtube_access_token):
    youtube = build('youtube', 'v3', developerKey=youtube_access_token)
    request = youtube.search().list(part='id', type='video', q=trackName, maxResults=1)
    response = request.execute()

    return response

def downloadVideos(VideoIDList):  
    for idx, ID in enumerate(VideoIDList):
        link = YouTube_URL + ID
        
        yt = YouTube(link).streams.first()
        authorName = YouTube(link).author
        print("Downloading", idx+1, "/", len(VideoIDList), " -", yt.title)

        fileName = authorName + ' - ' + yt.title
        validatedTitle = validateTitle(fileName)

        yt.download(output_path='out/Files', filename=validatedTitle + '.mp4')

        mp4VideoTitle = './out/Files/' + validatedTitle + '.mp4'
        mp3TrackTitle = './out/Files/' + validatedTitle + '.mp3'

        videoclip = VideoFileClip(mp4VideoTitle)
        
        audioclip = videoclip.audio
        audioclip.write_audiofile(mp3TrackTitle)

        audioclip.close()
        videoclip.close()

        os.remove(mp4VideoTitle)
    print("Files downloaded")

def validateTitle(yt_title):
    # Regex out some windows incompatible characters
    yt_title = re.sub(r'[? | $ | . | ! | < | > | - | *]', r' ', yt_title)
    print(yt_title)
    return yt_title 

getPlaylist(playlist_id, accessToken)
downloadVideos(VideoIDList)