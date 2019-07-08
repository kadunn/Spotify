
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
    ## for returning user saved tracks:
    # results = sp.current_user_saved_tracks()
    # for item in results['items']:
    #     track = item['track']
    #     print(track['name'] + ' - ' + track['artists'][0]['name'])
    results = sp.search(q='artist:' + 'weezer', type='artist')
    print(results)

else:
    print( "Can't get token for", username)
