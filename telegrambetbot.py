from football import Football
import pandas as pd
import datetime

today = datetime.datetime.strptime("2018-05-01T18:45:00Z", '%Y-%m-%dT%H:%M:%SZ')

football = Football("57b02f65320a40fbbf3fc24e554f552f")
fixtures = football.competition_fixtures("PL")['fixtures']

for game in fixtures:
	match_list = []
	game_time = datetime.datetime.strptime(game['date'], '%Y-%m-%dT%H:%M:%SZ')
	day_difference = (game_time-today).days
	if (7>day_difference>0):
		print ('****')

		hometeamstring = game['_links']['homeTeam']['href']
		hometeamcode = hometeamstring.split("/teams/")[1]
		awayteamstring = game['_links']['awayTeam']['href']
		awayteamcode = awayteamstring.split("/teams/")[1]
		hometeamcode = football.team(hometeamcode)['code']
		awayteamcode = football.team(awayteamcode)['code']


		teams = game['homeTeamName'] + "-" + game['awayTeamName']
		team_codes = hometeamcode + "-" + awayteamcode
		odds = "1/1"
		bets_data = {'friend_name' : ['omer','eran'],'team':[hometeamcode,awayteamcode],'bet':[10,10]}
		bets = pd.DataFrame(bets_data)
		teams_dict = {"teams":teams}
		team_codes_dict = {"team codes":team_codes}
		time_dict = {"time":str(game_time)}
		odds_dict = {"odds":odds}
		bets_dict = {"existing bets":bets}
		match_list = [teams_dict,team_codes_dict,time_dict,odds_dict,bets_dict]
		print(match_list)


