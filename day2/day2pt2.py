with open('input.txt') as f:
    string = f.readlines()

if __name__ == '__main__':
    total = 0
    teste = 0
    for i, line in enumerate(string):
        rounds = line.split(';')
        colors = ['red', 'green', 'blue']
        multiplication = 1
        number_of_cubes = [0, 0, 0]
        for round in rounds:
            for j, color in enumerate(colors):
                if round.find(color) != -1:
                    if round[round.find(color) - 3].isnumeric():
                        if int(number_of_cubes[j]) < int(round[round.find(color) - 3] + round[round.find(color) - 2]):
                            number_of_cubes[j] = int(round[round.find(color) - 3] + round[round.find(color) - 2])
                    else:
                        if int(number_of_cubes[j]) < int(round[round.find(color) - 2]):
                            number_of_cubes[j] = round[round.find(color) - 2]
        print(number_of_cubes)
        for n in number_of_cubes:
            multiplication = multiplication * int(n)
        print(multiplication)
        total = total + multiplication
    print(total)