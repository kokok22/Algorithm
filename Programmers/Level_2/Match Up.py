def solution(n,a,b):
    cnt = 1
    while True:
        if (a-1)//2 == (b-1)//2:
            return cnt
        else:
            a = (a-1)//2 + 1
            b = (b-1)//2 + 1
            cnt += 1

print(solution(8,4,7))