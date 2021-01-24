def gcd(a, b):
    if b == 0:
        return a
    else:
        return gcd(b, a % b)


def solution(arr):
    a = arr[0]

    for b in arr:
        if a < b:
            a, b = b, a
        a = a * b // gcd(a, b)

    return a

print(solution([2,6,8,14]))