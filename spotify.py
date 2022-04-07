
# FROM GITHUB: https://github.com/plamere/spotipy/blob/master/examples/my_top_tracks.py
# SPOTIPY MANUAL: https://spotipy.readthedocs.io/en/2.19.0/#module-spotipy.oauth2

import spotipy
from spotipy.oauth2 import SpotifyOAuth

scope = "user-library-read"

sp = spotipy.Spotify(auth_manager=SpotifyOAuth(scope=scope, 
                    redirect_uri= 'http://localhost/%22', 
                    client_id='13b99c641cb84422bf00e60ab6b60304', 
                    client_secret='d2f702d6d9604a94a1fcb35db4b869c4'))

# returns info about current user. Not necessary, but shows the API is connected
print(sp.me())

# supposed to return top tracks
ranges = ['short_term', 'medium_term', 'long_term']

for sp_range in ranges:
    print("range:", sp_range)
    results = sp.current_user_top_tracks(time_range=sp_range, limit=50)
    for i, item in enumerate(results['items']):
        print(i, item['name'], '//', item['artists'][0]['name'])
    print()
