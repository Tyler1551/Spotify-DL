# Spotify-DL
This application allows for users to mass download mp3 files using a spotify playlist link using Python.

## Installation
To install the application simply clone this repo with `git clone https://github.com/Tyler1551/Spotify-DL.git`  
Make sure Python3 is installed  
Next, install dependencies with `pip install -r requirements.txt`

## Usage
Before running the program you will need to set up a file called "credentials.json" this will be used to store Spotify and YouTube API credentials. The file should be formatted as follows:  
```
{
    "spotify_client_ID":"Your Spotify-Client-ID",
    "spotify_client_secret":"Your-Spotify-Client-Secret",
    "youtube_key":"Your-YouTube-API-Key"
}
```

Next we will run the program with `py main.py` in your terminal of choice and simply enter the link to your Spotify playlist. This will go through each of the tracks in the playlist and save them as .mp3 files under `./Files`
