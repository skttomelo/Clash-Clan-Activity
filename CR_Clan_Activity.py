import json
import requests
from settings import RA_API_KEY, RA_API_URL, CLAN

# Royale API Calls
'''
    https://api.royaleapi.com/clan/2U2GGQJ/history -- could be used to track which players are new which could then be cross checked with
    the official clash royale api to see which players joined during the last war based off time/date
'''
ra_headers = {"Accept":"application/json", "authorization":RA_API_KEY}

warlog = requests.get(RA_API_URL+'clan/'+CLAN+'/warlog', headers=ra_headers).json()
clanhistory = requests.get(RA_API_URL+'clan/'+CLAN+'/history', headers=ra_headers).json()
clanmembers = requests.get(RA_API_URL+'clan/'+CLAN, headers=ra_headers).json()

# consolidate these vars to a config file
inactive_wars_row = 3 # How many wars in a row can a player be inactive
donation_threshold = 50 # minimum donations a player will need before the hit the threshold minimum
whitelist = {}

# find which players have been inactive consec based off inactive_wars_row and return how many days in a row they have missed from the past 3 wars (excludes on-going)
def inactive_wars_consec(player_tag, inactive_times):
    consec_inactive = 0 # wars so far inactive
    current_war = 0 # will be used to keep track of how many wars we check
    for war in warlog: # loop through each war in the log
        in_war = True
        if current_war == inactive_times: # we have checked all the wars we needed too
            break
        for participant in war['participants']: # loop through participants in the war
            # check if they were in the war
            if player_tag != participant['tag']:
                in_war = False
            else:
                if (participant['battlesMissed'] != 0) and (participant['collectionDayBattlesPlayed'] != 3):
                    in_war = False
                else:
                    in_war = True
                break # we found the player so it's time to check the next war
        if in_war == False:
            consec_inactive += 1
        else:
            consec_inactive = 0
        current_war += 1
    return consec_inactive

# checks if a player joined during the last war
# in particular we care if the player joined after the collection day battle and before the end of the war
# that would mean that a player would be considered new if they joined within 24 hours prior to the war ending
# def is_new_player(player, war_end_time):
    
# count the total members, elders, and coleaders in clan
def rank_count():
    member = 0
    elder = 0
    coleader = 0
    for player in clanmembers['members']:
        if player['role'] == 'member':
            member += 1
        elif player['role'] == 'elder':
            elder += 1
        elif player['role'] == 'coLeader':
            coleader += 1
    return member,elder,coleader

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

with open('role_count.txt', 'w') as txt_file:
    member,elder,coleader = rank_count()
    data = 'Total Player Count: %s\nTotal Member Count: %a\nTotal Elder Count: %d\nTotal CoLeader Count = %e' % (clanmembers['memberCount'],member,elder,coleader)
    txt_file.write(data)
with open('warlog.json', 'w') as json_file:
    json.dump(warlog, json_file)
with open('clanmembers.json', 'w') as json_file:
    json.dump(clanmembers, json_file)
with open('player_donations.txt', 'w') as txt_file:
    for player in clanmembers['members']:
        p_data = '%s - %a: %d\n' % (player['tag'], player['name'], player['donations'])
        txt_file.write(p_data)
with open('player_war_inactivity.txt', 'w') as txt_file:
    for player in clanmembers['members']:
        inactivity = inactive_wars_consec(player['tag'], inactive_wars_row)
        if inactivity != 0:
            p_data = '%s - %a: %d\n' % (player['tag'], player['name'], inactivity)
            txt_file.write(p_data)