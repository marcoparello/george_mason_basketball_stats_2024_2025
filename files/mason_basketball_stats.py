from espn_scraper import*
from omni_scraper import*
from bart_torvik_scraper import*

#basically the workhorse, calls all the functions to get the stats with the appropriate urls
def get_mason_basketball_stats():
    #Women's Basketball
    print("------------------------------------------START ESPN'S GEORGE MASON WOMEN'S BASKETBALL STATS------------------------------- \n")
    get_espn_location_stats('https://site.api.espn.com/apis/site/v2/sports/basketball/womens-college-basketball/teams/2244')
    get_espn_schedule("https://site.api.espn.com/apis/site/v2/sports/basketball/womens-college-basketball/teams/2244/schedule")
    get_espn_game_stats("https://site.api.espn.com/apis/site/v2/sports/basketball/womens-college-basketball/teams/2244/statistics")
    print("------------------------------------------END ESPN'S GEORGE MASON WOMEN'S BASKETBALL STATS------------------------------- \n")

    print("------------------------------------------START OMNIRANKING'S GEORGE MASON WOMEN'S BASKETBALL STATS------------------------------- \n")
    get_omnirankings('https://www.omnirankings.com/wcb/Teams/George%20Mason.htm','https://omnirankings.com/wcb/Macro/NCAA%20Probabilities.htm',"wbb")
    print("------------------------------------------END OMNIRANKING'S GEORGE MASON WOMEN'S BASKETBALL STATS------------------------------- \n")

    print("------------------------------------------START BARTTORVIK'S GEORGE MASON WOMEN'S BASKETBALL STATS------------------------------- \n")
    get_player_stats("https://barttorvik.com/ncaaw/getadvstats.php?year=2025&specialSource=0&conyes=0&start=20241101&end=20250501&top=364&xvalue=&page=team&team=George+Mason")
    print("------------------------------------------END BARTTORVIK'S GEORGE MASON WOMEN'S BASKETBALL STATS------------------------------- \n")

    #Men's Basketball
    print("------------------------------------------START ESPN'S GEORGE MASON MEN'S BASKETBALL STATS------------------------------- \n")
    get_espn_location_stats('https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/teams/2244')
    get_espn_schedule("https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/teams/2244/schedule")
    get_espn_game_stats("https://site.api.espn.com/apis/site/v2/sports/basketball/mens-college-basketball/teams/2244/statistics")
    print("------------------------------------------END ESPN'S GEORGE MASON MEN'S BASKETBALL STATS------------------------------- \n")

    print("------------------------------------------START OMNIRANKING'S GEORGE MASON MEN'S BASKETBALL STATS------------------------------- \n")
    get_omnirankings('https://www.omnirankings.com/mcb/Teams/George%20Mason.htm','https://omnirankings.com/mcb/Macro/NCAA%20Probabilities.htm',"mbb")
    print("------------------------------------------END OMNIRANKING'S GEORGE MASON MEN'S BASKETBALL STATS------------------------------- \n")

    print("------------------------------------------START BARTTORVIK'S GEORGE MASON MEN'S BASKETBALL STATS------------------------------- \n")
    get_player_stats("https://barttorvik.com/getadvstats.php?year=2025&specialSource=0&conyes=0&start=20241101&end=20250501&top=364&xvalue=&page=team&team=George+Mason")
    print("------------------------------------------END BARTTORVIK'S GEORGE MASON MEN'S BASKETBALL STATS------------------------------- \n")

