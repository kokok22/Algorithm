## 달팽이 숫자 만들기

T = int(input())

for t in range(T):
    N = int(input())
    matrix = []

    for i in range(N):
        matrix.append([0]*N)
        matrix[0][i] = str(i+1)

    y = 0
    x = N-1
    num = N+1
    direct_x = 1
    direct_y = -1

    for j in range(N-1,0,-1):
        for i in range(2):
            if i == 0:
                direct_y *= -1
            else:
                direct_x *= -1

            for z in range(j):
                if i == 0:
                    y += direct_y
                else:
                    x += direct_x

                matrix[y][x] = str(num)
                num +=1

    print("#{}".format(t+1))
    for i in range(N):
        print(' '.join(matrix[i]))