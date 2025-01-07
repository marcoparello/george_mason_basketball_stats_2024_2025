
# import requests
import requests
# import parse from jsonpath_ng to parse the JSON data
from jsonpath_ng import parse

# overall record, home record, and away record
def get_espn_location_stats(url):
    # Define the API endpoint URL

    # Make a GET request to the API endpoint using requests.get()
    response = requests.get(url)
   
    # Put the response.json() content into a variable
    posts = response.json()
    #parse for record
    jsonpath_expr = parse('$..record[*]')

# Find all matches in the JSON structure
    matches = jsonpath_expr.find(posts)


# Extract and display records
    records = [match.value for match in matches]
    for i, record in enumerate(records, 1):
     
    
        for item in record['items']:
            
            print(f"{item['description']} ({item['type']}): {item['summary']}")
            for stat in item['stats']:
                print(f"  - {stat['name']}: {stat['value']}")
        print()
def get_espn_schedule(url):
     # Define the API endpoint URL

    # Make a GET request to the API endpoint using requests.get()
    response = requests.get(url)
   
    # Put the response.json() content into a variable
    posts = response.json()
    #parse for events
    jsonpath_expr = parse('$..events[*]')

# Find all matches in the JSON structure
    matches = jsonpath_expr.find(posts)
    records = [match.value for match in matches]
    winner = []
    loser = []
    score1 = [];
    score2 = [];
    

    for event in posts["events"]: 
        for competition in event["competitions"]:
            for teams in competition["competitors"]:
                
                try:
                   
                    if (teams["winner"] == True):
                        # add who won the game to winner array
                        winner.append(teams["team"]["nickname"])
                        # add the winners score to the score1 array
                        score1.append(teams["score"]["displayValue"])
                    else:
                        # add who lost the game to loser array
                        loser.append(teams["team"]["nickname"])
                        # add the losers score to the score2 array
                        score2.append(teams["score"]["displayValue"])
                        # print the winner, loser, and score of the game           
                  
               
                except KeyError:
                       pass
    #parse for leaders
    jsonpath_expr = parse('$..leaders[*]')
    matches = jsonpath_expr.find(posts)
    records = [match.value for match in matches]
    points = []
    rebounds = []
    assists = []
    for leaders in records:
        if leaders.get("name") == "points":
            points.append(f'The points leader was {leaders["leaders"][0]["athlete"]["displayName"]} with {leaders["leaders"][0]["value"]} points.')
        if leaders.get("name") == "rebounds":   
            rebounds.append(f'The rebounds leader was {leaders["leaders"][0]["athlete"]["displayName"]} with {leaders["leaders"][0]["value"]} rebounds.')
        if leaders.get("name") == "assists":
            assists.append(f'The assists leader was {leaders["leaders"][0]["athlete"]["displayName"]} with {leaders["leaders"][0]["value"]} assists.')

    print("\t \t GAME RESULTS")
    multiplier = 1
    for i in range(0, len(winner)):
        print(f'Game {multiplier}: Winner was {winner[i]}. Loser was {loser[i]}. Score was {score1[i]} to {score2[i]}. {points[i]} {rebounds[i]} {assists[i]}\n' )
        multiplier += 1
    
            
      
# General, Offensive, and Defensive stats          
def get_espn_game_stats(url):
        # Define the API endpoint URL

    # Make a GET request to the API endpoint using requests.get()
    response = requests.get(url)
   
    # Put the response.json() content into a variable
    posts = response.json()
    #parse for events
    jsonpath_expr = parse('$..categories[*]')

# Find all matches in the JSON structure
    matches = jsonpath_expr.find(posts)
    records = [match.value for match in matches]

    for stats in records:
        if stats.get("name") == "general":
            print("GENERAL STATS:")
            # iterate through the general stats and print them with the display name and display value
            for item in stats["stats"]:
                print(f'-  {item["displayName"]} {item["displayValue"]}')
        if stats.get("name") == "offensive":
            print("\n OFFENSIVE STATS: ")
            for item in stats["stats"]:
                # iterate through the offensive stats and print them with the display name and display value
                print(f'-  {item["displayName"]} {item["displayValue"]}')
           
        if stats.get("name") == "defensive":
            print("\n DEFENSIVE STATS: ")
            for item in stats["stats"]:
                # iterate through the defensive stats and print them with the display name and display value
                print(f'-  {item["displayName"]} {item["displayValue"]}')

