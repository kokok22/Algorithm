def solution(n):
    map = []
    maximum = int(n/2*(n+1))
    size = [i for i in range(1,maximum+1)]
    idx = 0

    for i in range(n):
        map.append([0]*(i+1))

    for i in range(n):
        map[i][0] = size[idx]
        idx += 1

    k = n-1
    flag = 1
    p = -1
    t1 = 1
    t2 = 2
    while k != 0:
        for i in range(k):
            # x축이 변함
            if flag%3==1:
                map[p][t1+i] = size[idx]

            # y축이 변함
            elif flag%3==2:
                map[t1-i][p] = size[idx]

            # p가 1씩 증가
            if flag%3==0:
                map[t2+i][p] = size[idx]

            idx +=1

        if flag%3==1:
            t1 = -(t1+1)
        elif flag%3==2:
            p *= -1
            t1 *= -1
        elif flag%3==0:
            p = -(p+1)
            t2 += 2

        # 반복횟수가 점점 줄어들음
        k -= 1
        # 방향 번경
        flag += 1

    answer = []
    for i in map:
        for j in i:
            answer.append(j)

    return answer



print(solution(10))