from __future__ import unicode_literals
import yt_dlp as youtube_dl
import os


ydl_opts = {
    'format': 'bestaudio/best',
    'postprocessors': [{
        'key': 'FFmpegExtractAudio',
        'preferredcodec': 'mp3',
        'preferredquality': '192',
    }],
    'ffmpeg-location': "ffmpeg",
}

def download_with_link(link, save_path):
    try:  
        os.mkdir(save_path)  
    except OSError as error:
        print(error)   
    ydl_opts['outtmpl'] = save_path + '/%(title)s.%(ext)s'

    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if type(link) == str:
            ydl.download([link])
        elif type(link) == list:
            ydl.download(link)
        else: return None
