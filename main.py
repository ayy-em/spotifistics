import json
import spotipy
from pprint import pprint
from spotipy.oauth2 import SpotifyOAuth


with open("credentials.json", "r") as credfile:
    crederoony = json.load(credfile)
    spotify_client_id = crederoony['spotify_client_id']
    spotify_client_secret = crederoony['spotify_client_secret']

spotify_redirect_url = "https://somethingreally.fun/spotify"
sp = spotipy.Spotify(auth_manager=SpotifyOAuth(client_id=spotify_client_id,
                                               client_secret=spotify_client_secret,
                                               redirect_uri=spotify_redirect_url,
                                               scope="user-library-read"))

results = sp.current_user_saved_tracks()
top_five_list = list()
print('Your 20 latest saved tracks are:')
for idx, item in enumerate(results['items']):
    track = item['track']
    if idx in range(0, 5):
        top_five_list.append(track['uri'])
    print(str('\t# ' + str(idx+1)), '>', track['artists'][0]['name'], " – ", track['name'])
print('------------')

recommended_tracks = sp.recommendations(seed_tracks=top_five_list, limit=5)
print('Here are 5 tracks for you to enjoy:')
for idz, rec_track in enumerate(recommended_tracks['tracks']):
    print('\t#', str(idz + 1), '>', str(rec_track['artists'][0]['name']), '-', str(rec_track['name']))
print("----------------------------")
userino = sp.current_user()
