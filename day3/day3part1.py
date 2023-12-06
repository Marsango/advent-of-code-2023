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


def manipulating_matrix(matrix):
    sum = 0
    for j, row in enumerate(matrix):
        i = 0
        while i < len(row) -1:
            nums = ''
            positions = []
            is_summable = False
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
                        if not matrix[j - 1][k].isnumeric() and matrix[j - 1][k] != '.':
                            is_summable = True
                    if not matrix[j][k].isnumeric() and matrix[j][k] != '.':
                        is_summable = True
                    if j != len(matrix) -1:
                        if not matrix[j + 1][k].isnumeric() and matrix[j + 1][k] != '.':
                            is_summable = True
                if is_summable == True:
                    sum += int(nums)
            elif i < len(row) -1:
                i += 1
    return sum

if __name__ == '__main__':
    print(manipulating_matrix(creating_matrix()))