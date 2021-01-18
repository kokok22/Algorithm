def solution(n):
    num=set(range(2,n+1))

    for i in range(2,n+1):
        if i in num:
            # 소수의 배수들을 다 제거해준다.
            num-=set(range(2*i,n+1,i))
    return len(num)

    return answer