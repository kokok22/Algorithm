def solution(m, n, board):
    ## 기존의 모양 대로 말고 x가 같은 애들끼리 같은 리스트에 들어가도록 다시 리스트 만들기
    ## 좌표를 모두 구한다음 set을 통해 겹치는 것 제거 set의 길이만큼 cnt++해주고
    ## y좌표를 기준으로 sorting하고 위에 있는 애들 먼저 pop으로 제거해준다. 그럼 index 안꼬임
    ## 각 라인별로 max값을 저장해 놓아서 index out of range발생하지 않도록 해주자

    maps = []
    line = [m] * n
    # x가 같은 애들끼리 같은 리스트에 넣어줬음.
    # board와 maps의 좌표는 반대로 되어 있다.
    for x in range(n):
        temp = []
        for y in range(m):
            temp.append(board[y][x])
        maps.append(temp)

    cnt = 0
    while True:
        remove = []
        for x in range(n - 1):
            for y in range(m - 1):
                if line[x] >= m - y and line[x + 1] >= m - y:
                    if maps[x][y] == maps[x + 1][y + 1] and maps[x][y] == maps[x][y + 1] and maps[x][y] == maps[x + 1][
                        y]:
                        if [x, y] not in remove:
                            remove.append([x, y])
                        if [x, y + 1] not in remove:
                            remove.append([x, y + 1])
                        if [x + 1, y] not in remove:
                            remove.append([x + 1, y])
                        if [x + 1, y + 1] not in remove:
                            remove.append([x + 1, y + 1])

        if not remove:
            break

        for x, y in remove:
            cnt += 1
            y1 = y
            line[x] -= 1
            while y1 >= 1:
                maps[x][y1] = maps[x][y1 - 1]
                y1 -= 1

    return cnt


print(solution(4,5,["CCBDE", "AAADE", "AAABF", "CCBBF"]))