with open('input.txt') as f:
    string = f.readlines()


def get_winning_numbers(j):
    total_winning_numbers_match = 0
    winning_array = []
    my_numbers_array = []
    numbers = string[j].strip('\n').split(' ')
    is_separate_symbol_finded = False
    for number in numbers:
        if number == '|':
            is_separate_symbol_finded = True
        if is_separate_symbol_finded and number.isnumeric():
            winning_array.append(int(number))
        elif not is_separate_symbol_finded and number.isnumeric():
            my_numbers_array.append(int(number))
    for my_number in my_numbers_array:
        for winning in winning_array:
            if my_number == winning:
                total_winning_numbers_match += 1

    return total_winning_numbers_match


def total_value_of_cards():
    sum = 0
    number_of_executions = []
    for i in range(len(string)):
        number_of_executions.append(1)
    for j, card in enumerate(string):
            for k in range(j + 1, j + get_winning_numbers(j) + 1):
                number_of_executions[k] += 1 * number_of_executions[j]
                print(number_of_executions)
    for exec in number_of_executions:
        sum += int(exec)
    print(number_of_executions)
    return sum


if __name__ == '__main__':
    print(total_value_of_cards())
