with open('input.txt') as f:
    string = f.readlines()

def last_find(string, find_this):
    index = string.find(find_this)
    if(index != -1):
        index += len(find_this)
        while string.find(find_this, index) != -1:
            index = string.find(find_this, index)
            index += len(find_this)
    return index

if __name__ == '__main__':
    total = 0
    for line in string:
        num_string = ['one', 'two', 'three', 'four', 'five', 'six', 'seven', 'eight', 'nine']
        number = ['1', '2', '3', '4', '5', '6', '7', '8', '9']
        line = line.strip('\n')
        first_digit_position = 99999
        first_digit = 0
        last_digit_position = -1
        last_digit = 0
        index = 0
        for i in range(0, 9):
            print(f'{i}. posicao: {last_digit_position} numero: {num_string[i]}')
            if first_digit_position > line.find(number[i]) and line.find(number[i]) != -1:
                first_digit_position = line.find(number[i])
                first_digit = number[i]
            if first_digit_position > line.find(num_string[i]) and line.find(num_string[i]) != -1:
                first_digit_position = line.find(num_string[i])
                first_digit = number[i]
            if last_digit_position < last_find(line, number[i]) and line.find(number[i]) != -1:
                last_digit_position = last_find(line, number[i])
                last_digit = number[i]
            if last_digit_position < last_find(line, num_string[i]) and line.find(num_string[i]) != -1:
                last_digit_position = last_find(line, num_string[i])
                last_digit = number[i]
        aux = str(first_digit) + str(last_digit)
        total = total + int(aux)
total
