
# FROM GITHUB: https://github.com/plamere/spotipy/blob/master/examples/my_top_tracks.py
# SPOTIPY MANUAL: https://spotipy.readthedocs.io/en/2.19.0/#module-spotipy.oauth2

from requests import get
import spotipy
from spotipy.oauth2 import SpotifyOAuth
import os
import urllib.request

# scope = "user-library-read"

# sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, 
#                     redirect_uri= 'http://localhost/%22', 
#                     client_id='13b99c641cb84422bf00e60ab6b60304', 
#                     client_secret='d2f702d6d9604a94a1fcb35db4b869c4'))

# # returns info about current user. Not necessary, but shows the API is connected
# print(sp.me())

# # supposed to return top tracks
# ranges = ['short_term', 'medium_term', 'long_term']

# for sp_range in ranges:
#     print("range:", sp_range)
#     results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
#     for i, item in enumerate(results['items']):
#         print(i, item['name'], '//', item['artists'][0]['name'])
    # print()



def getAlbumCovers(filepath):
    scope = 'user-read-recently-played user-read-private user-top-read user-read-currently-playing'
    spotify = spotipy.Spotify(auth_manager=SpotifyOAuth(redirect_uri= 'http://localhost/%22', 
                                                        client_id='13b99c641cb84422bf00e60ab6b60304', 
                                                        client_secret='d2f702d6d9604a94a1fcb35db4b869c4',
                                                        scope=scope))

    ## Get the current user's profile information and their top x tracks.
    user = spotify.me()
    # print(user)

    ## Create a temp spotify directory if it doesn't already exist.
    if not os.path.exists(filepath):
        os.makedirs(filepath)

    ## Get the current users top 25 tracks and download the album art for each.
    top_tracks = spotify.current_user_top_tracks(time_range='long_term', limit=25)
    # print(f'top_tracks = {top_tracks}')
    for i, item in enumerate(top_tracks['items']):
        # print(item)
        urllib.request.urlretrieve(item['album']['images'][0]['url'], filepath + (os.path.sep + item['album']['name']).replace(" ", "") + ".jpeg")


if __name__ == '__main__':
    getAlbumCovers(os.getcwd() + os.path.sep + 'datafiles')
