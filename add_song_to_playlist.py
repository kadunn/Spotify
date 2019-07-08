import pprint
import sys

import spotipy
import spotipy.util as util



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
    playlist_id = '5qu9v0IiwRjb1psTyTLNAY'
    track_ids = ["spotify:track:1pAyyxlkPuGnENdj4g7Y4f", "spotify:track:7D2xaUXQ4DGY5JJAdM5mGP"]
    results = sp.user_playlist_add_tracks(username, playlist_id, track_ids)
    print(results)

else:
    print("Can't get token for", username)
