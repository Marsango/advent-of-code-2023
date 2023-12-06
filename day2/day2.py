with open('input.txt') as f:
    string = f.readlines()

if __name__ == '__main__':
    total = 0
    teste = 0
    for i, line in enumerate(string):
        is_game_valid = True
        rounds = line.split(';')
        min_cube = [9999, 9999, 9999]
        colors = ['red', 'green', 'blue']
        for round in rounds:
            number_of_cubes = [0, 0, 0]
            for j,color in enumerate(colors):
                if round.find(color) != -1:
                    if round[round.find(color) - 3].isnumeric():
                        number_of_cubes[j] = round[round.find(color) - 3] + round[round.find(color) - 2]
                    else:
                        number_of_cubes[j] = round[round.find(color) - 2]
            print(number_of_cubes)
            if int(number_of_cubes[0]) > 12 or int(number_of_cubes[1]) > 13 or int(number_of_cubes[2]) > 14:
                is_game_valid = False
                break;
        if is_game_valid:
            total = total + i + 1
    print(total)