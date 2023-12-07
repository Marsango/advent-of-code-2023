def input_function():
    with open('input.txt') as f:
        string = f.readlines()
    time = []
    distance = []
    for j, line in enumerate(string):
        aux = line.strip('\n').split(" ")
        for a in aux:
            if (a.isnumeric()):
                if j == 0:
                    time.append(int(a))
                else:
                    distance.append(int(a))
    return time, distance

def calculate_distance(time, distance):
    multiplication = 1
    for i in range(len(time)):
        count_ways_of_win = 0
        for j in range(1, time[i] + 1):
            if (time[i] - j) * j > distance[i]:
                count_ways_of_win += 1
        multiplication *= count_ways_of_win
    return multiplication

if __name__ == '__main__':
    print(calculate_distance(input_function()[0], input_function()[1]))


    ##(time - pressed_time) * pressed_time > distance