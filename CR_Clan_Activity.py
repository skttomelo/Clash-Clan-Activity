import json
import requests
from settings import API_KEY, API_URL, CLAN

warlog = requests.get(API_URL+'clans/'+CLAN+'/warlog', headers={"Accept":"application/json", "authorization":API_KEY}, params={"limit":3}).json()
clanmembers = requests.get(API_URL+'clans/'+CLAN+'/members', headers={"Accept":"application/json", "authorization":API_KEY}).json()

# consolidate these vars to a config file
inactive_wars_row = 3 # How many wars in a row can a player be inactive
donation_threshold = 50 # minimum donations a player will need before the hit the threshold minimum
# TODO: add a time variable for how long a player is allowed to be offline before their inactivity is recorded

# find which players have been inactive consec based off inactive_wars_row and return how many days in a row they have missed from the past 3 wars (excludes on-going)
def inactive_wars_consec(player_tag, inactive_times):
    consec_inactive = 0 # wars so far inactive
    for war in warlog['items']:
        in_war = True
        for participant in war['participants']:
            if player_tag != participant['tag']:
                in_war = False
            else:
                in_war = True
                break
        if in_war == False:
            consec_inactive += 1
        else:
            consec_inactive = 0
    return consec_inactive

with open('warlog.json', 'w') as json_file:
    json.dump(warlog, json_file)
with open('clanmembers.json', 'w') as json_file:
    json.dump(clanmembers, json_file)
with open('player_donations.txt', 'w') as txt_file:
    for player in clanmembers['items']:
        p_data = '%s - %a: %d\n' % (player['tag'], player['name'], player['donations'])
        txt_file.write(p_data)
with open('player_war_inactivity.txt', 'w') as txt_file:
    for player in clanmembers['items']:
        inactivity = inactive_wars_consec(player['tag'], inactive_wars_row)
        if inactivity != 0:
            p_data = '%s - %a: %d\n' % (player['tag'], player['name'], inactivity)
            txt_file.write(p_data)