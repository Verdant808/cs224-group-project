
import os
import spotipy
import urllib.request

from spotipy.oauth2 import SpotifyOAuth

def getAlbumCovers(filepath):
    scope = 'user-read-recently-played user-read-private user-top-read user-read-currently-playing'
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="4609e546effa44be903f7064e1a393f4",
                                                        client_secret="f1348c1b838545b8965b4c69537126e7",
                                                        redirect_uri="http://localhost:8080/callback",
                                                        scope=scope))

    ## Get the current user's profile information and their top x tracks.
    # user = spotify.me()

    ## Create a temp spotify directory if it doesn't already exist.
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    ## Get the current users top 25 tracks and download the album art for each.
    top_tracks = spotify.current_user_top_tracks(time_range='long_term', limit=25)
    for i, item in enumerate(top_tracks['items']):
        urllib.request.urlretrieve(item['album']['images'][0]['url'], filepath + (os.path.sep + item['album']['name']).replace(" ", "") + ".jpeg")