'''
    Problem 1:
    Consider your entire calibration document. What is the sum of all of the calibration values?
    Combine the first digit and the last digit to make the value, then add them

    Ex:
    1abc2           = 12
    pqr3stu8vwx     = 38
    a1b2c3d4e5f     = 15
    treb7uchet      = 77 (notice 1 number will turn into the duplicate)

    In this example, the calibration values of these four lines are 12, 38, 15, and 77. Adding these together produces 142.

    For this solution, I will strip the one line from a txt file, strip all non-numeric chars out, then take first and last out and concat them
'''
stripped_list = []

def read_data():
    with open('./data_day1.txt', 'r') as file:
        for line in file:
            numbers = line.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'})
            numbers = numbers.strip('\n')
            stripped_list.append(numbers)

def parse_and_add(list):
    total = 0

    for number in list:
        length = len(number)
        # print(f'Concat: {number[0] + number[length-1]}') # debug but leaving in
        total += int(number[0] + number[length-1])
        # print(f'Running total: {total}')
    
    print(f'Final Total: {total}')


'''
    Problem 2:
    Add in the spelled out numbers and include this in the calculation
    Problem only states that one, two, three, four, five, six, seven, eight, and nine count to this

    adding in a statement that will replace these out, too
'''

substr_list = ["one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]

def read_data_2():
    total_val = 0
    with open('./data_day1.txt', 'r') as file:
        for line in file:
            numbers = line.strip('\n')
            # print(f'Before replace: {line}')

            for substr in substr_list:
                # print(f'Substr: {substr}, Value: {str(substr_list.index(substr) + 1)}')
                numbers = numbers.replace(substr, str(substr_list.index(substr) + 1))

            # numbers = numbers.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'})
            # print(f'After replace: {numbers}\n')
            total_val = strip_helper(numbers, total_val)
            print(f'Running Val: {total_val + 580}')

def strip_helper(numbers, total_val):
    numbers = numbers.translate({ord(i): None for i in 'abcdefghijklmnopqrstuvwxyz'})
    total_val += int(numbers[0] + numbers[len(numbers)-1])
    # print(numbers)

    return total_val

if __name__ == "__main__":
    read_data()
    parse_and_add(stripped_list)
    read_data_2()