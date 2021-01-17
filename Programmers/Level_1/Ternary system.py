def solution(n):
    answer = 0
    third = ''

    while n > 0:
        third += str(n % 3)
        n = n // 3

    count = 1

    for th in third[::-1]:
        answer += int(th) * count
        count *= 3

    return answer

print(solution(45))