## 3 6 9 게임

num = int(input())
check = ['3','6','9']

for i in range(1,num+1):
    flag = 0
    for char in str(i):
        if char in check:
            print("-",end="")
            flag = 1

    if flag==0:
        print(i,end="")

    print(" ",end="")