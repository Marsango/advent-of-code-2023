with open('input.txt') as f:
    string = f.readlines()

if __name__ == '__main__':
    total = 0
    teste = 0
    for i, line in enumerate(string):
        is_round_valid = True
        rounds = line.split(';')
        for round in rounds:
            number_of_green = 0
            if round.find('green') != -1:
                if round[round.find('green') - 3].isnumeric():
                    number_of_green = round[round.find('green') - 3] + round[round.find('green') - 2]
                else:
                    number_of_green = round[round.find('green') - 2]
            number_of_red = 0
            if round.find('red') != -1:
                if round[round.find('red') - 3].isnumeric():
                    number_of_red = round[round.find('red') - 3] + round[round.find('red') - 2]
                else:
                    number_of_red = round[round.find('red') - 2]
            number_of_blue = 0
            if round.find('blue') != -1:
                if round[round.find('blue') - 3].isnumeric():
                    number_of_blue = round[round.find('blue') - 3] + round[round.find('blue') - 2]
                else:
                    number_of_blue = round[round.find('blue') - 2]
            print(f'{i}. {number_of_red} {number_of_green} {number_of_blue}')
            if int(number_of_red) > 12 or int(number_of_green) > 13 or int(number_of_blue) > 14:
                is_round_valid = False
                break;
        if(is_round_valid == True):
            total = total + i + 1
    print(total)