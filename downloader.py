from __future__ import unicode_literals
import yt_dlp as youtube_dl
import os


ydl_opts = {
    'writethumbnail': True,
    'format': 'bestaudio/best',
    'postprocessors': [{
            'key': 'FFmpegExtractAudio',
            'preferredcodec': 'mp3',
            'preferredquality': '192',
        },{
            'key': 'FFmpegMetadata',
            'add_metadata': True,
        },{
            'key': 'EmbedThumbnail',
            'already_have_thumbnail': True
        }
    ],
    'ffmpeg-location': "ffmpeg.exe",    
}

def download_with_link(link, save_path):
    try:  
        os.mkdir(save_path)  
    except OSError as error:
        print(error)   
    ydl_opts['outtmpl'] = save_path + '/%(title)s.%(ext)s'
    
    with youtube_dl.YoutubeDL(ydl_opts) as ydl:
        if type(link) == str:
            # info = ydl.extract_info(link, True)
            # embed_cover_art(info["title"])
            ydl.download([link])
        # elif type(link) == list:
        #     ydl.download(link)
        else: return None


