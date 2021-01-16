# 압축 풀기

T =int(input())

for t in range(T):
    N = int(input())

    char = []
    for i in range(N):
        char.append(list(map(str,input().strip(' ').split(' '))))


    print("#{}".format(t+1))
    count = 0
    for i in range(N):
        for j in range(int(char[i][1])):
            count += 1
            print(char[i][0],end="")
            if count ==10:
                count =0
                print()

    print()
