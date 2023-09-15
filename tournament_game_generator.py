def tournamentGameGenerator(teams_list, wins_list):
    tournament_games = []
    win_dict = {key:value for key,value in zip(wins_list,teams_list)}
    sorted_win_list = sorted(wins_list)
    idx2 = int(len(wins_list)/2)
    home_keys = sorted_win_list[:idx2]
    away_keys = sorted_win_list[idx2:][::-1]

    for home,away in zip(home_keys,away_keys):
        tournament_games.append(f'Home: {win_dict[home]} VS Away: {win_dict[away]}')

    return tournament_games

no_of_teams = 0
teams_list = []
wins_list = []
number_of_games = 0
while True:
    no_of_teams = int(input('Enter the number of teams in the tournament: '))
    if no_of_teams >= 2:
        break
    else:
        print('The minimum number of teams is 2, try again.')

for i in range(1,no_of_teams+1):
    while True:
        team = str(input(f'Enter the name for team #{i}: '))

        if len(team) < 2:
            print('Team names must have at least 2 characters, try again.')

        elif len(list(team.split())) > 2:
            print('Team names may have at most 2 words, try again.')

        else:
            teams_list.append(team)
            break
while True:
    number_of_games = int(input('Enter the number of games played by each team: '))
    if number_of_games < no_of_teams - 1:
        print('Invalid number of games. Each team plays each other at least once in the regular season, try again.')
    else:
        break

for team in teams_list:
    while True:
        win_count = int(input(f'Enter the number of wins Team {team} had: '))
        if win_count < 0:
            print('Minimum number of wins is 0. Please try again.')

        elif win_count > number_of_games:
            print("It's impossible to win more games than the number of games that was played. try again.")

        else:
            wins_list.append(win_count)
            break

print('Generating the games to be played in the first round of the tournament...')
tournament_games = tournamentGameGenerator(teams_list, wins_list)
for game in tournament_games:
    print(game)