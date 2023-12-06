with open('input.txt') as f:
    string = f.readlines()


def last_find(string, find_this):
    index = string.find(find_this)
    if (index != -1):
        index += len(find_this)
        while string.find(find_this, index) != -1:
            index = string.find(find_this, index)
            index += len(find_this)
    return index


def creating_matrix():
    for i, s in enumerate(string):
        string[i] = s.strip('\n')
    matrix = []

    for line in string:
        a = []
        for c in line:
            a.append(c)
        matrix.append(a)
    return matrix

def is_any_number_near_of_gear(gear_location, num1, matrix):
    row_location = gear_location[0]
    column_location = gear_location[1]
    if column_location == 0:
        start = 0
    else:
        start = column_location - 1
    if column_location == len(matrix[0]) -1:
        end = len(matrix[0]) + 1
    else:
        end = column_location + 2
    for j in range(row_location -1, row_location + 2):
        row = matrix[j]
        i = 0
        while i < len(row) - 1:
            nums = ''
            positions = []
            if row[i].isnumeric() and i != len(row) - 1:
                while row[i].isnumeric() and i < len(row):
                    nums = nums + row[i]
                    positions.append(i)
                    i += 1
                    if i == len(row):
                        break
                for position in positions:
                    if position in range (start, end):
                        return nums
            elif i < len(row) -1:
                i += 1
    return 0

def manipulating_matrix(matrix):
    sum = 0
    for j, row in enumerate(matrix):
        i = 0
        while i < len(row) -1:
            nums = ''
            num2 = 0
            positions = []
            is_gear = False
            if row[i].isnumeric() and i != len(row) - 1:
                while row[i].isnumeric() and i < len(row):
                    nums = nums + row[i]
                    positions.append(i)
                    i += 1
                    if i == len(row):
                        break
                if positions[0] == 0:
                    start = 0
                else:
                    start = positions[0] -1
                if positions[-1] == len(row) - 1: ## cuidar
                    end = positions[-1]
                else:
                    end = positions[-1] + 1
                for k in range(start, end + 1):
                    if j != 0:
                        if matrix[j - 1][k] == '*':
                            num2 = is_any_number_near_of_gear([j-1, k], nums, matrix)
                    if matrix[j][k] == '*':
                       num2 = is_any_number_near_of_gear([j, k], nums, matrix)
                    if j != len(matrix) -1:
                        if matrix[j + 1][k] == '*':
                            num2 = is_any_number_near_of_gear([j+1, k], nums, matrix)
                if num2 != 0 and nums != num2:
                    print(f'num: {str(nums)} num2:{str(num2)}')
                    sum += int(nums) * int(num2)
            elif i < len(row) -1:
                i += 1
    return sum

if __name__ == '__main__':
    print(manipulating_matrix(creating_matrix()))