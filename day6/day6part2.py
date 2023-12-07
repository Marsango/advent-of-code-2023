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
                    time.append(a)
                else:
                    distance.append(a)
    return int("".join(time)), int("".join(distance))

def calculate_distance(time, distance):
    multiplication = 1
    count_ways_of_win = 0
    for j in range(1, time + 1):
        if (time - j) * j > distance:
            count_ways_of_win += 1
    multiplication *= count_ways_of_win
    return multiplication

if __name__ == '__main__':
    print(calculate_distance(input_function()[0], input_function()[1]))


    ##(time - pressed_time) * pressed_time > distance