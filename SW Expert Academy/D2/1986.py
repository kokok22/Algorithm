## 홀수는 더하고 짝수는 빼자

def total(num):
    remain = num%2
    quotient = num//2

    if remain == 1:
        return quotient+1
    else:
        return quotient*-1


T = int(input())

for t in range(T):
    num = int(input())

    print("#{} {}".format(t+1, total(num)))