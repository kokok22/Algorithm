# 정렬

T = int(input())

for t in range(T):
    N = int(input())

    nums = list(map(int,input().strip(' ').split(' ')))
    nums.sort()

    nums = list(map(str, nums))

    print("#{} {}".format(t+1,' '.join(nums)))