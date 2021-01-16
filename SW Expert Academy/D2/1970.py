## 거스름돈

T = int(input())
units = [50000, 10000, 5000, 1000, 500, 100, 50, 10]

for t in range(T):
    money = int(input())
    changes = []

    for unit in units:
        count = money//unit
        changes.append(str(count))

        money -= unit*count

    print("#{}".format(t+1))
    print(' '.join(changes))