## 날짜 계산기
month = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

T = int(input())

for t in range(T):
    total = 0

    m1, d1, m2, d2 = list(map(int, input().strip(' ').split(' ')))

    if m1 == m2:
        total += d2-d1+1
    else:
        total += month[m1-1]-d1+1
        total += d2
        total += sum(month[m1:m2-1])

    print("#{} {}".format(t+1, total))