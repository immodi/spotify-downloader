from spotipy import Spotify
from spotipy.oauth2 import SpotifyClientCredentials

CLIENT_ID = "a664e292dd94406cbca496b6f4ada586"
CLIENT_SECRET = "58ed3db92fa5467ca9d76487ba573316"

client = SpotifyClientCredentials(client_id=CLIENT_ID, client_secret=CLIENT_SECRET)
sp = Spotify(client_credentials_manager=client)

def __get_playlist_tracks__(playlist_link) -> dict:
    playlist_id = playlist_link.split("/")[-1].split("?")[0]
    results = sp.playlist_tracks(playlist_id)
    tracks = results['items']
    while results['next']:
        results = sp.next(results)
        tracks.extend(results['items'])
    return tracks


def get_songs_names(playlist_link):
    tracks_response = __get_playlist_tracks__(playlist_link)
    tracks = []
    for track in tracks_response:
        track_name = track["track"]["name"]
        try: artist_name = track["track"]["album"]["artists"][0]["name"]
        except TypeError: artist_name = ""
        tracks.append(f"{track_name} {artist_name}")

    return tracks

