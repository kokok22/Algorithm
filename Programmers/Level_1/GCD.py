def solution(n, m):
    def gcd(a, b):
        if a % b == 0:
            return b
        else:
            return gcd(b, a % b)

    if n < m:
        n, m = m, n
    g = gcd(n, m)
    l = n * m // g

    return [g, l]