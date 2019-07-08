import xmltodict
import pprint
import json
from collections import OrderedDict
from datetime import datetime
from datetime import timedelta

document_file = open('/Users/kendalldunn/Desktop/Projects/Spotify/Library.xml', "r") # Open a file in read-only mode
original_doc = document_file.read() # read the file object
document = xmltodict.parse(original_doc) # Parse the read document string
tracks = document['dict']['dict']['dict'] # list of ordered dicts

tags_strings = ['Name', 'Artist', 'Album Artist', 'Composer', 'Album','Genre','Kind']
tags_ints = ['Total Time','Play Count','Skip Count']

tracks_stripped = []
int_list = ['Track ID','Size','Total Time','Disc Number','Disc Count','Track Number',
                'Track Count','Year','Bit Rate','Sample Rate','Play Count','Play Date','Skip Count'
                'Normalization','Artwork Count','Track Type','Remote']

for i in range(len(tracks)):

    if not 'Playlist Only' in tracks[i]['key']:

        strings_dict = {}
        all_found = True

        # Make sure all of the strings are in the keys
        for l in tags_strings:
            if not l in tracks[i]['key']:
                all_found = False

        if all_found:
            for k in range(len(tags_strings)):

                # add Genre and Name from Strings
                strings_dict[tags_strings[k]] = tracks[i]['string'][k]

            # index of Play Count (int) if it in in Keys
            ind = tracks[i]['key'].index('Play Count') if 'Play Count' in tracks[i]['key'] else -1
            count_int = 0
            found = False
            j = 0
            while j < len(tracks[i]['key']) and not found and ind >= 0:
                if tracks[i]['key'][j] in int_list:
                    # Counts up in Ints until finds 'Play Count'
                    if tracks[i]['key'][j] == 'Play Count':
                        found = True
                    count_int += 1
                j+= 1
            # If 'Play Count' found, add to dict
            if ind >= 0:
                strings_dict['Play Count'] = int(tracks[i]['integer'][count_int-1])

            ind = tracks[i]['key'].index('Skip Count') if 'Skip Count' in tracks[i]['key'] else -1
            count_int = 0
            found = False
            j = 0
            while j < len(tracks[i]['key']) and not found and ind >= 0:
                if tracks[i]['key'][j] in int_list:
                    if tracks[i]['key'][j] == 'Skip Count':
                        found = True
                    count_int += 1
                j+= 1
            if ind >= 0 and 'Play Count' in strings_dict.keys():
                strings_dict['Skip Count'] = int(tracks[i]['integer'][count_int-1])
                strings_dict['Play Ratio'] = strings_dict['Play Count'] / strings_dict['Skip Count']
            else:
                strings_dict['Play Ratio'] = 50

            # index of Total Time (int) if it in in Keys
            ind = tracks[i]['key'].index('Total Time') if 'Total Time' in tracks[i]['key'] else -1
            count_int = 0
            found = False
            j = 0
            while j < len(tracks[i]['key']) and not found and ind >= 0:
                if tracks[i]['key'][j] in int_list:
                    # Counts up in Ints until finds 'Total Time'
                    if tracks[i]['key'][j] == 'Total Time':
                        found = True
                    count_int += 1
                j+= 1
            # If 'Total Time' found, add to dict
            if ind >= 0:
                strings_dict['Total Time'] = int(tracks[i]['integer'][count_int-1])

        tracks_stripped.append(strings_dict)

with open('tracks.json', 'w') as f:
    json.dump(tracks_stripped, f)
