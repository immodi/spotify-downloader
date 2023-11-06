import crawler
import downloader
import spotify
import sys

# PLAYLIST_LINK = "https://open.spotify.com/playlist/7dyygRNkq3QUB0EliWthu6?si=c32f497fef884d0e"
PLAYLIST_LINK = sys.argv[1]
OUTPUT_DIR = sys.argv[2]
tracks_name = spotify.get_songs_names(PLAYLIST_LINK)

for song in tracks_name:
    song_link = crawler.search(song)
    downloader.download_with_link(song_link, OUTPUT_DIR)