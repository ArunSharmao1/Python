import itertools
import random
'''itertools: Library for creating iterators for efficient looping.
random: Library for generating random numbers.'''


def possible_match_count(teams):
    # Calculate the total number of possible matches between teams
    return len(list(itertools.combinations(teams, 2)))
'''Purpose: Calculates the total number of possible matches between teams.
How: Uses itertools.combinations to generate all possible pairs of teams, then counts them.'''



def schedule_matches(teams, total_matches):
    # Generate all possible match combinations
    possible_matches = list(itertools.combinations(teams, 2))
    if total_matches > len(possible_matches):
        return "Not enough teams to schedule the requested number of matches."
    
    random.shuffle(possible_matches)
    
    scheduled_matches = []
    last_team = None
    
    while len(scheduled_matches) < total_matches:
        for match in possible_matches:
            if match[0] != last_team and match[1] != last_team:
                scheduled_matches.append(match)
                last_team = match
                possible_matches.remove(match)
                break
        else:
            return "Unable to schedule matches without consecutive games for any team."
    
    return scheduled_matches
'''Purpose: Schedules matches between teams.
How:
Generates all possible match combinations.
Shuffles the list of possible matches.
Schedules matches ensuring no team plays back-to-back games.
Returns a list of scheduled matches.'''



def update_points_table(points_table, match, result):
    team1, team2 = match
    points_table[team1]['matches'] += 1
    points_table[team2]['matches'] += 1

    if result == 'draw':
        points_table[team1]['draw'] += 1
        points_table[team2]['draw'] += 1 
        points_table[team1]['points'] += 1  # Assuming 1 point for a draw
        points_table[team2]['points'] += 1  # Assuming 1 point for a draw
    elif result == team1: 
        points_table[team1]['win'] += 1
        points_table[team1]['points'] += 2  # Assuming 2 points for a win
        points_table[team2]['loss'] += 1
    else:
        points_table[team2]['win'] += 1
        points_table[team2]['points'] += 2  # Assuming 2 points for a win
        points_table[team1]['loss'] += 1     
'''Purpose: Updates the points table based on match results.
How:
Increments the number of matches played by each team.
Updates win, loss, draw counts, and points based on the match result.'''




def display_points_table(points_table):
    # Display the points table header
    print("\nPoints Table:")
    print(f"{'Team':<10} {'Matches':<8} {'Wins':<5} {'Losses':<7} {'Draws':<6} {'Points':<6}")
    sorted_table = sorted(points_table.items(), key=lambda x: x[1]['points'], reverse=True)
    # Display each team's stats in the points table
    for team, stats in sorted_table:
        print(f"{team:<10} {stats['matches']:<8} {stats['win']:<5} {stats['loss']:<7} {stats['draw']:<6} {stats['points']:<6}")
'''Purpose: Displays the points table.
How:
Prints headers for the table.
Sorts teams by points in descending order.
Prints each team's statistics.'''




def main(): 
    num_teams = int(input("Enter the number of teams: "))
    
    teams = []
    for i in range(num_teams):
        team_name = input(f"Enter name for team {i+1}: ")
        teams.append(team_name)
    
    total_possible_matches = possible_match_count(teams)
    print(f"\nTotal possible matches: {total_possible_matches}")
    
    total_matches = int(input(f"Enter the total number of matches to be scheduled (max {total_possible_matches}): "))
    
    points_table = {team: {'matches': 0, 'win': 0, 'loss': 0, 'draw': 0, 'points': 0} for team in teams}
    
    matches = schedule_matches(teams, total_matches)
    
    if isinstance(matches, str):
        print(matches)
        return
    
    print("\nScheduled Matches:")
    for idx, match in enumerate(matches, 1):
        print(f"Match {idx}: {match[0]} vs {match[1]}")
    
    print("\nEnter the results of the matches:")
    for idx, match in enumerate(matches, 1):
        while True:
            result = input(f"Enter the result for Match {idx} ({match[0]} vs {match[1]}) (Enter 'draw' or the winning team name): ").strip()
            if result in [match[0], match[1], 'draw']:
                break
            else:
                print("Invalid input. Please enter 'draw' or the name of the winning team.")
        update_points_table(points_table, match, result)
    
    display_points_table(points_table)
    
if __name__ == "__main__":
    main()
'''Purpose: The main function orchestrates the entire process.
How:
Takes user input for the number of teams, team names, and total matches.
Calculates possible matches and schedules matches.
Updates the points table based on match results provided by the user.
Finally, displays the points table.'''