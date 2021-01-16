T = int(input())
check = {0,1,2,3,4,5,6,7,8,9}

for t in range(T):
    num = int(input())
    result = set()
    count = 1

    while True:
        temp = num * count

        for n in str(temp):
            result.add(int(n))

        if result == check:
            num = temp
            break

        count += 1

    print("#{} {}".format(t+1, num))