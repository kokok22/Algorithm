def calculate(A,B,N,M):
    max_value = -1000000

    for i in range(M-N+1):
        total = 0
        for j in range(N):
            total += A[j]*B[i+j]

        if max_value < total:
            max_value = total

    return max_value

T = int(input())

for t in range(T):
    N, M = list(map(int, input().strip(' ').split(' ')))

    A = list(map(int, input().strip(' ').split(' ')))
    B = list(map(int, input().strip(' ').split(' ')))

    if M < N:
        result = calculate(B,A,M,N)
    else:
        result = calculate(A,B,N,M)

    print("#{} {}".format(t+1,result))
