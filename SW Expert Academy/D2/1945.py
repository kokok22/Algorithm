T = int(input())

for t in range(T):
    num = int(input())

    decimal = [2,3,5,7,11]
    result = [0,0,0,0,0]

    idx = 0
    while True:
        if idx>4 or num == 0:
            break
        if num % decimal[idx] == 0:
            result[idx] += 1
            num = num//decimal[idx]
        else:
            idx += 1

    result = list(map(str, result))

    print("#{} {}".format(t+1, ' '.join(result)))
