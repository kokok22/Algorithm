def solution(w,h):
    def gcd(n,m):
        if n%m ==0:
            return m
        else:
            return gcd(m,n%m)

    if h > w:
        w, h = h, w

    num = gcd(w,h)
    a, b = w//num, h//num

    return w*h-num*(a+b-1)


print(solution(12,8))