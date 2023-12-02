'''
    Problem 1:
    Add the Game ID of POSSIBLE games together, each game will be limited by
    12 red cubes, 13 green cubes, and 14 blue cubes
'''

'''
    Notes for how I constructed mutable data:
    made a default 'game_dict' constructed with a key value pair for GameID: Game Dictionary
    GameID is Integer
    Game Dictionary is a Python List of entries of each pull Key value pair with CubeCount: Color
'''

POSSIBILITIES = {
    'red': 12,
    'green': 13,
    'blue': 14
}

game_dict = {}

def parse_data():
    with open('./Day2/input.txt', 'r') as data:
        # Since we know the dataset will have the same game on each line, we can strip the 'Game ID:'

        for line in data:
            current_line = line.strip('\n') # removes cring newline char
            strip_game_id = current_line.split(':')
            game_id = strip_game_id[0].translate({ord(i): None for i in 'abcdefgGhijklmnopqrstuvwxyz'}).strip(' ')
            # print(game_id) # debug line
            
            current_game_data = parse_game(strip_game_id[1])

            game_dict.update({int(game_id): current_game_data})
        
        # print(game_dict)


def parse_game(current_game):
    each_pull = []
    game_iteration = current_game.split(';') # splits the line into each pull

    for iteration in game_iteration:
        cube_pulls = iteration.split(',') # splits each pull
        # we know that there is a leading space on every game and pull

        game_data = {
            'red': 0,
            'green': 0,
            'blue': 0
        }

        for color in cube_pulls:
            dict_entry = color.replace(' ', '', 1)
            dict_entry = dict_entry.split(' ') # now we have number of cubes, and color
            game_data.update({dict_entry[1]: game_data.get(dict_entry[1]) + int(dict_entry[0])})
        
        each_pull.append(game_data)
    
    return each_pull 

def calculate_possibilities():
    impossible_game_ids = [] # inverse from the impossible games, subtract from a thoretical 5050 (sum 1:-> 100)

    for game_id in game_dict:
        for game_pulls in game_dict.get(game_id):
            if game_pulls.get('red') > POSSIBILITIES.get('red'):
                print(f'IMPOSSIBLE GameID: {game_id}')
                impossible_game_ids.append(game_id)
                break # invlaidates whole set thereafter
            elif game_pulls.get('green') > POSSIBILITIES.get('green'):
                print(f'IMPOSSIBLE GameID: {game_id}')
                impossible_game_ids.append(game_id)
                break # invlaidates whole set thereafter
            elif game_pulls.get('blue') > POSSIBILITIES.get('blue'):
                print(f'IMPOSSIBLE GameID: {game_id}')
                impossible_game_ids.append(game_id)
                break # invlaidates whole set thereafter
            
    
    # need to remove duplicates, oops
    impossible_game_ids = list(set(impossible_game_ids))
    print(impossible_game_ids)

    # summation of 1 to 100 is 5050
    summation = 5050
    for id in impossible_game_ids:
        summation -= id

    print(f'Total Value: {summation}')

'''
    Problem 2:
    Now take each game, determine each game's minimum possible cubes to make a valid game
    multiply the lcd of the red, green. blue cubes
    then add them to the total
'''

def calculate_cubes():
    minimum_game_sets = {
        "red": 0,
        "green": 0,
        "blue": 0
    }

    game_powers = []
    total_powers = 0

    for game_id in game_dict:
        for game_pulls in game_dict.get(game_id):
            if game_pulls.get('red') > minimum_game_sets.get('red'):
                minimum_game_sets.update({'red': game_pulls.get('red')})
            
            if game_pulls.get('green') > minimum_game_sets.get('green'):
                minimum_game_sets.update({'green': game_pulls.get('green')})

            if game_pulls.get('blue') > minimum_game_sets.get('blue'):
                minimum_game_sets.update({'blue': game_pulls.get('blue')})

        game_powers.append(minimum_game_sets.get('red') * minimum_game_sets.get('green') * minimum_game_sets.get('blue'))
        minimum_game_sets.update({'red': 0})
        minimum_game_sets.update({'green': 0})
        minimum_game_sets.update({'blue': 0})

        print(f'GameID: {game_id}, Game Power: {game_powers[game_id-1]}')
    
    for power in game_powers:
        total_powers += power
    
    print(f'Total Summation of Game Powers: {total_powers}')

if __name__ == "__main__":
    parse_data()
    # calculate_possibilities()
    calculate_cubes()