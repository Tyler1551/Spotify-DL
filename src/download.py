from pytube import YouTube
from moviepy.editor import *

import re
import os

# Regex out some windows incompatible characters
def validateTitle(yt_title):
    yt_title = re.sub(r"[?|$|.|!|<|>|-|*|/|']", r' ', yt_title)
    return yt_title 

# Take video ID from the list. Download each mp4, convert to mp3 and remove .mp4
def downloadVideos(VideoIDList):  
    for idx, ID in enumerate(VideoIDList):
        link = 'https://www.youtube.com/watch?v=' + ID
        
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