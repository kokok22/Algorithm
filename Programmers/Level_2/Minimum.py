def solution(A, B):
    A.sort()
    B.sort(reverse=True)

    sum = 0
    for a, b in zip(A, B):
        sum += a * b

    return sum

print(solution([1, 4, 2], [5, 4, 4]))