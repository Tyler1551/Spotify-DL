import spotify as sp
import download as dl

# Set headers to send Spotify Auth token
accessToken = sp.getAuth()

# get the list of youtube video ID's based on search
VideoIDList = sp.getPlaylist(accessToken)
dl.downloadVideos(VideoIDList)