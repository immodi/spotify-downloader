from requests import get
from yt_dlp import YoutubeDL

YDL_OPTIONS = {'format': 'bestaudio', 'noplaylist':'True'}

def search(arg) -> str:
    query = f"{arg} lyrics"
    
    with YoutubeDL(YDL_OPTIONS) as ydl:
        try:
            get(query) 
        except:
            video = ydl.extract_info(f"ytsearch:{query}", download=False)['entries'][0:5]
        else:
            video = ydl.extract_info(query, download=False)[0]
    
       
    return video[0]["webpage_url"]

