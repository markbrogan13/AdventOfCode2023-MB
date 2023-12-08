'''
    Problem 1: 
    Find the number of of ways you can beat the top score
    multiply the numbers together

    Time:        44     70     70     80
    Distance:   283   1134   1134   1491
'''
import math
import time

times = []
distance = []

def read_data():
    with open('./Day6/input.txt', 'r') as races:
        lines = races.readlines()
        time_str = lines[0][5:].strip('\n').strip(' ').split('    ')
        distance_str = lines[1][9:].strip('\n').strip(' ').split('   ')

        for index, time in enumerate(time_str):
            times.append(int(time.strip(' ')))
            distance.append(int(distance_str[index]))

def read_data_2():
    with open('./Day6/input.txt', 'r') as races:
        lines = races.readlines()
        long_time = lines[0][5:].strip('\n').translate({ord(i): None for i in ' '})
        distance = lines[1][9:].strip('\n').translate({ord(i): None for i in ' '})
        beat_the_ai_2(int(long_time), int(distance))

def beat_the_ai():
    flower_power = 1
    for index, ms in enumerate(times):
        lower_end = math.ceil(distance[index] / ms)

        full_set = {}
        for i in range(lower_end, ms):
            hold_distance = i * (ms - i)
            if hold_distance > distance[index]:
                full_set.update({i: hold_distance})
        
        flower_power *= len(full_set)
        print(flower_power)
        
def beat_the_ai_2(long_time, distance):
    tic = time.perf_counter()

    full_set = {}
    for i in range(1, long_time):
            hold_distance = i * (long_time - i)
            if hold_distance > distance:
                full_set.update({i: hold_distance})
    
    toc = time.perf_counter()
    print(f'Total Win Conditions: {len(full_set)}, time this function took: {toc - tic:0.4f} seconds')

if __name__ == "__main__":
    read_data()
    beat_the_ai()
    read_data_2()