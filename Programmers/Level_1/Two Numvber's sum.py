def solution(a, b):
    if a < b:
        a, b = b, a

    answer = (a + b) * (a - b + 1) // 2

    return answer