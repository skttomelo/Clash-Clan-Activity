import json
import requests
from settings import API_KEY, API_URL, CLAN

warlog = requests.get(API_URL+'clans/'+CLAN+'/warlog', headers={"Accept":"application/json", "authorization":API_KEY}, params={"limit":10})
clanmembers = requests.get(API_URL+'clans/'+CLAN+'/members', headers={"Accept":"application/json", "authorization":API_KEY})

with open('warlog.json', 'w') as json_file:
    json.dump(warlog.json(), json_file)
with open('clanmembers.json', 'w') as json_file:
    json.dump(clanmembers.json(), json_file)
with open('player_donations.txt', 'w') as txt_file:
    for player in clanmembers.json()['items']:
        p_data = '%s: %d \n' % (player['tag'],player['donations'])
        txt_file.write(p_data)
