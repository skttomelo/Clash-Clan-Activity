import json
import requests
from settings import RA_API_KEY, RA_API_URL, CR_API_KEY, CR_API_URL, CLAN

# Royale API Calls
'''
    https://api.royaleapi.com/clan/2U2GGQJ/history -- could be used to track which players are new which could then be cross checked with
    the official clash royale api to see which players joined during the last war based off time/date
'''
ra_headers = {"Accept":"application/json", "authorization":RA_API_KEY}
ra_test = requests.get(RA_API_URL+'player/8C9CQ00Y', headers=ra_headers).json()
with open('stats royale test.json', 'w') as test:
    json.dump(ra_test, test)

#Oficial Clash Royale API Calls
cr_headers = {"Accept":"application/json", "authorization":CR_API_KEY}
warlog = requests.get(CR_API_URL+'clans/'+CLAN+'/warlog', headers=cr_headers, params={"limit":3}).json()
clanmembers = requests.get(CR_API_URL+'clans/'+CLAN+'/members', headers=cr_headers).json()

# consolidate these vars to a config file
inactive_wars_row = 3 # How many wars in a row can a player be inactive
donation_threshold = 50 # minimum donations a player will need before the hit the threshold minimum
whitelist = {}
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

def is_accessible(path, mode='r'):
    """
    Check if the file or directory at `path` can
    be accessed by the program using `mode` open flags.
    """
    try:
        f = open(path, mode)
        f.close()
    except IOError:
        return False
    return True

# TODO: implement whitelist.json and remove entries when 7 days have past since the date_of_return
if is_accessible('whitelist.json') == True:
    with open('whitelist.json', 'r') as json_file:
        whitelist = json.load(json_file)
else:
    print('whitelist.json doesn\'t exist')

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