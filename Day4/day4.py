'''
    Problem 1:
    which of the numbers you have appear in the list of winning numbers. 
    The first match makes the card worth one point and each match after 
    the first doubles the point value of that card.

    Clean the data into a list of winning numbers and numbers you have
    create a list of matches 
    for each element in numbers you have check if in winning list
    if there is a winning number, immediately start at 1 point
    then take the lenght of the of that list
    if len(matches) == 0
    for _ in range(1, len(matches) - 1):
'''

winning_card_points = []

def get_current_card():
    with open('./Day4/input.txt', 'r') as games:
        for card in games:
            set_numbers = card.split('|')
            winning_numbers = set_numbers[0][10:].split(' ') # will type cast to int in helper func
            
            for index, value in enumerate(winning_numbers):
                if winning_numbers[index] == '':
                    winning_numbers.pop(index)
            
            card_numbers = set_numbers[1][1:].strip('\n').split(' ')
            for index_c, value_c in enumerate(card_numbers):
                if card_numbers[index_c] == '':
                    card_numbers.pop(index_c)
            
            calculate_card_points(winning_numbers, card_numbers)

def calculate_card_points(winning_set, your_set):
    matches = []
    for value in your_set:
        if value in winning_set:
            matches.append(value)
    
    if len(matches) <= 0:
        winning_card_points.append(0)
    elif len(matches) == 1:
        winning_card_points.append(1)
    else:
        points = 1
        for _ in range(1, len(matches)):
            points *= 2
        winning_card_points.append(points)

def calculate_points():
    total = 0
    for value in winning_card_points:
        total += value
    
    print(f'Total Value: {total}')

if __name__ == "__main__":
    get_current_card()
    calculate_points()