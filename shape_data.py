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

tags_strings = ['Name', 'Artist', 'Album Artist','Composer', 'Album','Genre','Kind']
tags_dates = ['Play Date UTC']
tags_ints = ['Play Count','Skip Count']

tracks_stripped = []
int_list = ['Track ID','Size','Total Time','Disc Number','Disc Count','Track Number',
                'Track Count','Year','Bit Rate','Sample Rate','Play Count','Play Date','Skip Count'
                'Normalization','Artwork Count','Track Type','Remote']

one_year_ago = datetime.now() - timedelta(days=365)
for i in range(len(tracks)):

    if not 'Playlist Only' in tracks[i]['key']:

        strings_dict = {}
        all_found = True
        for l in tags_strings:
            if not l in tracks[i]['key']:
                all_found = False
        if all_found:
            for k in range(len(tags_strings)):
                strings_dict[tags_strings[k]] = tracks[i]['string'][k]
            ind = tracks[i]['key'].index('Play Count') if 'Play Count' in tracks[i]['key'] else -1
            count_int = 0
            found = False
            j = 0
            while j < len(tracks[i]['key']) and not found and ind >= 0:
                if tracks[i]['key'][j] in int_list:
                    if tracks[i]['key'][j] == 'Play Count':
                        found = True
                    count_int += 1
                j+= 1
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
            strings_dict['Play Date'] = datetime.strptime(tracks[i]['date'][2], '%Y-%m-%dT%H:%M:%SZ')
            strings_dict['Time Since Last Play'] = datetime.now() - strings_dict['Play Date']
            if strings_dict['Time Since Last Play'] <= timedelta(days=365) and strings_dict['Play Ratio'] > 10:
                tracks_stripped.append(strings_dict)


print(len(tracks_stripped))
print(*tracks_stripped, sep='\n')
