## 어디에 단어가 들어갈 수 있을까
## 빈칸 찾기
## brute force


def check(mini_map, N, K):
    total = 0
    for i in range(N):
        count_x = 0
        count_y = 0

        for j in range(N):
            if mini_map[i][j]==1:
                count_x += 1
            else:
                if count_x ==K:
                    total +=1
                count_x = 0

            if mini_map[j][i] == 1:
                count_y += 1

            else:
                if count_y == K:
                    total += 1
                count_y = 0

        if count_x == K:
            total += 1
        if count_y == K:
            total += 1

    return total


def make_map(N):
    result = []

    for i in range(N):
        result.append(list(map(int, input().strip(' ').split(' '))))
    return result


T =int(input())

for t in range(T):
    N, K = list(map(int, input().strip(' ').split(' ')))
    mini_map = make_map(N)

    print("#{} {}".format(t+1,check(mini_map, N, K)))