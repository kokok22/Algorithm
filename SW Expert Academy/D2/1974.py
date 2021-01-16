## 스도쿠 검증


def isSudoku(sudoku):
    sum_squ = [0] * 9

    for i in range(9):
        sum_x = 0
        pre_x = 0

        sum_y = 0
        pre_y = 0

        sel = i//3*3

        for j in range(9):
            idx = sel+j//3
            sum_squ[idx] += sudoku[i][j]

            if pre_x == sudoku[i][j] or pre_y == sudoku[j][i]:
                return False
            sum_x += sudoku[i][j]
            sum_y += sudoku[j][i]

        if sum_x != 45 or sum_y != 45:
            return False

    if sum_squ.count(45) != 9:
        return False

    return True

T = int(input())

for t in range(T):
    sudoku = []

    for i in range(9):
        sudoku.append(list(map(int, input().strip(' ').split(' '))))

    print("#{} {}".format(t+1, int(isSudoku(sudoku))))
