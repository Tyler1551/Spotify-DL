import youtube as yt

import requests
import json
import os

with open('credentials.json') as f:
    contents = json.load(f)
    Spotify_client_ID = contents['spotify_client_ID']
    Spotify_client_secret = contents['spotify_client_secret']

# Authentication and headers 
def getAuth():
    res = requests.post("https://accounts.spotify.com/api/token", {
    'grant_type': 'client_credentials',
    'client_id' : Spotify_client_ID,
    'client_secret' : Spotify_client_secret,
    })

    resData = res.json()
    accessToken = resData['access_token']

    return accessToken

def getHeaders(accessToken):
    headers = {
        'Authorization' : 'Bearer {token}'.format(token=accessToken)
    }

    return headers

# We need a method to get a list of tracks in a playlist and extract the track ID. We will use this to get the artist and track name
def getPlaylist(accessToken):
    playlist_link = input("Enter Spotify Playlist Link: ")
    playlist_id = playlist_link[34:56]

    r = requests.get('https://api.spotify.com/v1/' + 'playlists/' + playlist_id, headers=getHeaders(getAuth()))
    rJson = r.json()
    total_tracks = rJson['tracks']['total']

    print("Total Tracks: ", total_tracks)
    print()
    
    ID_List = []
    VideoIDList = []
    
    for i in range(total_tracks):
        track_id = rJson['tracks']['items'][i]['track']['id']
        ID_List.append(track_id)

    for song in ID_List:
        trackName = getTrackInfo(song, accessToken)
        results = yt.getTrack(trackName, yt.getYoutubeKey())
        trackID = results['items'][0]['id']['videoId']
        VideoIDList.append(trackID)
    
    return VideoIDList

def getTrackInfo(track_id, accessToken):
    r = requests.get('https://api.spotify.com/v1/' + 'tracks/' + track_id, headers=getHeaders(accessToken))
    rJson = r.json()

    TrackName = rJson['name']
    Artist = rJson['artists'][0]['name']
    return Artist + ' - ' + TrackName