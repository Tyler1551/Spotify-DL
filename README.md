# Spotify-DL
This application allows for users to mass download mp3 files using a spotify playlist link using Python, Spotify and YouTube API's.

## Installation
To install the application simply clone this repo with `git clone https://github.com/Tyler1551/Spotify-DL.git`  
Make sure Python3 is installed  
Next, install dependencies with `pip install -r requirements.txt`

## Usage
Before running the program you will need to set up a file called "credentials.json" this will be used to store Spotify and YouTube API credentials. The file should be formatted as follows:  
```
{
    "spotify_client_ID":"YOUR-SPOTIFY-API-CLIENT-ID",
    "spotify_client_secret":"YOUR-SPOTIFY-CLIENT-SECRET",
    "youtube_key":"YOUR-YOUTUBE-API-KEY"
}
```

To run the application use `python main.py`  
This will go through each of the tracks in the playlist and save them as .mp3 files under  
`./out/files/`
