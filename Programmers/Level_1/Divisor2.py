import math

def solution(n):
    result = set()

    for i in range(1, int(math.sqrt(n))+1):
        if n % i == 0:
            result.add(i)
            result.add(n // i)

    return sum(result)

print(solution(10))

