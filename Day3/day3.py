'''
    Problem 1:
    There are lots of numbers and symbols you don't really understand, 
    but apparently any number adjacent to a symbol, 
    even diagonally, is a "part number" and should be included in your sum. 
    (Periods (.) do not count as a symbol.)

    Considering a sliding window solution:
    - start on line 2
    - check previous line
    - check next line
    - Corner case of final line, add in a keyword when referencing the file is at an end
'''
summation_numbers = []

def edit_end_of_file():
    with open('./Day3/input.txt', 'a') as f:
        f.write('\nend')

def read_data():
    with open('./Day3/input.txt', 'r') as data:
        lines = data.readlines() # list to provide each line
        for linenum in range(1, len(lines) - 1): # iterate over each line number
            previous_line = lines[linenum - 1]
            current_line = lines[linenum]
            next_line = lines[linenum + 1]
            
            if linenum == 1:
                parse_lines(previous_line, current_line, next_line, True, False)
            elif linenum == len(lines) - 1:
                parse_lines(previous_line, current_line, next_line, False, True)
            else:
                parse_lines(previous_line, current_line, next_line, False, False)

def parse_lines(prev, current, next_, is_first, is_last):
    previous_line = prev.strip('\n')
    current_line = current.strip('\n')
    next_line = next_.strip('\n')

    '''
    Take the current_line, scan for the indicies of where special chars are
    look for a number:
        Previous line:  i - 1, i, i + 1
        Current line:   i - 1, i, i + 1
        Next Line:      i - 1, i, i + 1

    How to get the whole number associated with touching a special character?
    '''
    special_char_index_previous = []
    special_char_index_current = []
    special_char_index_next = []
    special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '?', '_', '=', ',', '<', '>', '/']
    if is_first:
        for index, char in enumerate(previous_line):
            if char in special_characters:
                special_char_index_previous.append(index)
        for index, char in enumerate(current_line):
            if char in special_characters:
                special_char_index_current.append(index)
        
        #TODO: Add in the numbers that have adjacency to previous line
    elif is_last:
        for index, char in enumerate(current_line):
            if char in special_characters:
                special_char_index_current.append(index)
        for index, char in enumerate(next_line):
            if char in special_characters:
                special_char_index_next.append(index)

        #TODO: Add in the numbers that have adjacency to next line
    else:
        for index, char in enumerate(previous_line):
            if char in special_characters:
                special_char_index_previous.append(index)
        for index, char in enumerate(current_line):
            if char in special_characters:
                special_char_index_current.append(index)
        for index, char in enumerate(next_line):
            if char in special_characters:
                special_char_index_next.append(index)
        
        #TODO: Add in the numbers that have adjacency to the current line
    
        





if __name__ == "__main__":
    # edit_end_of_file() # Runs once over all iterations
    read_data()