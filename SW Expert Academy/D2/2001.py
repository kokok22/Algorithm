## 파리퇴치
## 효율적으로 풀고 싶다...


def create_map(M):
    result = []

    for i in range(M):
        temp = list(map(int, input().split(' ')))
        result.append(temp)

    return result

T = int(input())

for t in range(T):
    M, N = list(map(int,input().split(' ')))
    mini_map = create_map(M)

    max = 0

    for i in range(M-N+1):
        for j in range(M-N+1):
            total = 0
            for x in range(i,i+N):
                for y in range(j,j+N):
                    total += mini_map[x][y]

            if total>max:
                max = total

    print("#{} {}".format(t+1,max))