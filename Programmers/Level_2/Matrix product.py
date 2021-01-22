def solution(arr1, arr2):
    x1, y1 = len(arr1[0]), len(arr1)
    x2, y2 = len(arr2[0]), x1

    answer = []
    for i in range(y1):
        answer.append([0]*x2)

    for y in range(y1):
        for x in range(x2):
            for i in range(x1):
                answer[y][x] += arr1[y][i]*arr2[i][x]

    return answer;


print(solution([[2, 3, 2], [4, 2, 4], [3, 1, 4]], [[5, 4, 3], [2, 4, 1], [3, 1, 1]]))