
# FROM GITHUB: https://github.com/plamere/spotipy/blob/master/examples/my_top_tracks.py
# SPOTIPY MANUAL: https://spotipy.readthedocs.io/en/2.19.0/#module-spotipy.oauth2

import os
import re
import spotipy
import urllib.request

from spotipy.oauth2 import SpotifyOAuth

def getAlbumCovers(filepath):
    scope = 'user-read-recently-played user-read-private user-top-read user-read-currently-playing'
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id="291af71203bb4b7e9a3cb87aae46d4c2",
                                                        client_secret="be0c68852f0a4a9c9e71d6764bf7d1b3",
                                                        redirect_uri="http://localhost:8080/callback",
                                                        scope=scope))

    # Create a temp spotify directory if it doesn't already exist.
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    # Get the current users top 25 tracks and download the album art for each.
    top_tracks = spotify.current_user_top_tracks(time_range='long_term', limit=25)
    for i, item in enumerate(top_tracks['items']):
        urllib.request.urlretrieve(item['album']['images'][0]['url'], filepath + (os.path.sep + re.sub('[^A-Za-z0-9]+', '', item['album']['name'])) + ".jpeg")

    # Get the current users playlist artwork
    result = spotify.current_user_playlists(limit=50, offset=0)
    for i, item in enumerate(result['items']):
        urllib.request.urlretrieve(item['images'][0]['url'], filepath + (os.path.sep + re.sub('[^A-Za-z0-9]+', '', item['name'])) + ".jpeg")