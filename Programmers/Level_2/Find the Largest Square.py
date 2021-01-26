def solution(board):
    for i in range(1, len(board)):
        for j in range(1, len(board[0])):
            if board[i][j] >= 1:
                board[i][j] = min(board[i - 1][j], board[i][j - 1], \
                                  board[i - 1][j - 1]) + 1

    return max([num for row in board for num in row]) ** 2



## 내가 처음에 짰던 코드, 문제는 통과했는데 효율성에서 탈락

#
# def solution(board):
#     n = len(board)
#     m = len(board[0])
#
#     answer = 0
#
#     for y in range(n):
#         for x in range(m):
#
#             if board[y][x] == 1:
#                 idx = 1
#
#                 while y + idx < n and x + idx < m:
#                     if board[y + idx][x + idx] == 1:
#                         idx += 1
#                     else:
#                         break
#                 idx -= 1
#
#                 flag = False
#
#                 for id in range(idx, 0, -1):
#                     for i in range(1, id + 1):
#                         if board[y + id - i][x + id] == 0 or board[y + id][x + id - i] == 0:
#                             flag = True
#                             break
#
#                     if flag == True:
#                         break
#                 else:
#                     if answer < (idx + 1) ** 2:
#                         answer = (idx + 1) ** 2
#
#     return answer