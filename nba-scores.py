from requests import get
from pprint import PrettyPrinter

BASE_URL = "https://data.nba.net"
ALL_JSON = "/prod/v1/today.json"
# ALL_JSON = "/prod/v1/2018/teams/{{}}/roster.json"
bulls = '1610612741'
printer = PrettyPrinter()


def get_links():
    data = get(BASE_URL + ALL_JSON).json()
    links = data['links']
    return links


# get_links()
# printer.pprint(get_links())


def get_scoreboard():
    scoreboard = get_links()['currentScoreboard']
    games = get(BASE_URL + scoreboard).json()['games']

    for game in games:
        home_team = game['hTeam']
        away_team = game['vTeam']
        clock = game['clock']
        period = game['period']

        print("------------------------------------------------")
        print(
            f"{home_team['triCode']} vs {away_team['triCode']}")
        print(f"{home_team['score']} - {away_team['score']}")
        print(f"{clock} - {period['current']}")


def get_stats():
    stats = get_links()['leagueTeamStatsLeaders']
    teams = get(
        BASE_URL + stats).json()['league']['standard']['regularSeason']['teams']

    teams = list(filter(lambda x: x['name'] != 'Adelaide', teams))
    teams = list(filter(lambda x: x['name'] != "Ra'anana", teams))

    # teams.sort(key=lambda x: int(x['ppg']['rank']))

    # printer.pprint(teams[0].keys())
    for i, team in enumerate(teams):
        id = team['teamId']
        name = team['name']
        nickname = team['nickname']
        ppg = team['ppg']['avg']

        print(f"{i + 1}. {id} - {name} - {nickname} - {ppg}")

    #  TeamID for the Bulls: 1610612741

# get_stats()


# def roster():
# roster = get_links()['leagueRosterPlayers']
# team_roster = get(BASE_URL + roster).json()['league']['standard']

# # for team in team_roster:
# #     first = team['firstName']
# #     last = team['lastName']
# #     te = team['teams']
# #     print("-----------------")
# #     print(f"{first} - {last} - {te}")
# # printer.pprint(tr.keys())
# # break

# # printer.pprint(team_roster[0].keys())
# printer.pprint(team_roster[0].keys())


# roster()


def team_roster():
    roster = get_links()['leagueSchedule']
    all_star = get(BASE_URL + roster).json()['league']['standard']

    printer.pprint(all_star[0].keys())

    for star in all_star:
        home = star['hTeam']

        print(home)
        break


team_roster()
team_roster()