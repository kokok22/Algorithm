def solution(board, moves):
    stack = []
    answer = 0

    for move in moves:
        for line in board:
            if line[move - 1] != 0:

                if len(stack) > 0 and stack[-1] == line[move - 1]:
                    stack.pop()
                    answer += 2

                else:
                    stack.append(line[move - 1])

                line[move - 1] = 0
                break

    return answer


board = [[0,0,0,0,0],[0,0,1,0,3],[0,2,5,0,1],[4,2,4,4,2],[3,5,1,3,1]]
moves = [1,5,3,5,1,2,1,4]

print(solution(board, moves))