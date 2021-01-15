## 파스칼의 삼각형 만들기

def pascal(height=1):
    pre = [1]
    now = []

    # height가 1인 경우
    if height == 1:
        print(1)
        return

    # height가 2 이상인 경우
    for j in range(height):
        now = []
        for i in range(j+1):
            if i==0:
                now.append(0+pre[i])
            elif i == j:
                now.append(0+pre[i-1])
            else:
                now.append(pre[i]+pre[i-1])

        pre = now
        for num in pre:
            print(num, end=" ")
        print()


T = int(input())

for i in range(T):
    height = int(input())
    print("#{}".format(i+1))
    pascal(height)