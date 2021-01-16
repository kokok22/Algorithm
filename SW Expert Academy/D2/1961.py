## 숫자 배열 회전

T = int(input())

for t in range(T):
    N = int(input())

    matrix = []

    for i in range(N):
        matrix.append(list(map(str, input().strip(' ').split(' '))))

    first = []
    half = []
    third = []

    for i in range(N):
        num1 = ''
        num2 = ''
        num3 = ''

        for j in range(N):
            num1 += matrix[N-j-1][i]
            num2 += matrix[N-i-1][N-j-1]
            num3 += matrix[j][N-i-1]

        first.append(num1)
        half.append(num2)
        third.append(num3)

    print("#{}".format(t+1))

    for i in range(N):
        print(first[i], half[i], third[i])