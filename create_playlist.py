import pprint
import spotipy
import spotipy.util as util

SPOTIPY_CLIENT_ID=''
SPOTIPY_CLIENT_SECRET=''
SPOTIPY_REDIRECT_URI=''
username = ''
scope = ''

token = util.prompt_for_user_token(
                            username,
                            scope,
                            client_id=SPOTIPY_CLIENT_ID,
                            client_secret=SPOTIPY_CLIENT_SECRET,
                            redirect_uri=SPOTIPY_REDIRECT_URI
                            )

if token:
    sp = spotipy.Spotify(auth=token)
    sp.trace = False
    playlist_name = 'test_playlist'
    playlist_description = 'first playlist made using API'
    playlists = sp.user_playlist_create(username, playlist_name, public=True)
    pprint.pprint(playlists)
else:
    print("Can't get token for", username)
