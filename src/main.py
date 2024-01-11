import spotify as sp
import youtube as yt
import download as dl

# Set headers to send Spotify Auth token
accessToken = sp.getAuth()
header = sp.getHeaders(accessToken)

# get the list of youtube video ID's based on search
VideoIDList = sp.getPlaylist(accessToken)
dl.downloadVideos(VideoIDList)