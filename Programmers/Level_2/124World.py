def solution(n):
    num = [1, 2, 4]
    answer = ''

    while n:
        answer += str(num[(n - 1) % 3])
        n = (n - 1) // 3

    return answer[::-1]

print(solution(100))