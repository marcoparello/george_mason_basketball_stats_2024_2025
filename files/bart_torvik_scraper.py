# requests
import requests

def get_player_stats(url):
    #headers to bypass security
    headers = {
    'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10.12; rv:55.0) Gecko/20100101 Firefox/55.0',
}
    response = requests.get(url,headers)
    # extract player stats array from the response
    player_stats = response.json()
    # store player stats in an array
   
    # loop through the player stats
    for player in player_stats:
        print(f"\n{player[0]} is {player[26]} and plays {player[-2]}. Their jersey number is {player[27]}. Their average stats are as follows:")
        print(f'\tPoints Per Game: {player[-3]:.1f}')
        print(f'\tPercentage Of Minutes Played: {player[4]}')
        print(f'\tAssists: {player[11]}')
        print(f'\tBlocks: {player[22]}')
        print(f'\tSteals: {player[23]}')
        print(f'\tOffensive Rebounds: {player[9]}')
        print(f'\tDefensive Rebounds: {player[10]}')
        print(f'\tFree Throw Percentage: {player[15]}')
        print(f'\t2 Point Shot Percentage: {player[18]}')
        print(f'\tclose 2 Point Shot Percentage: {player[40]}')
        print(f'\tFar 2 Point Shot Percentage: {player[41]}')
        print(f'\t3 Point Shot Percentage: {player[21]}')

