## 최대 최소를 제외한 나머지의 평균값을 구하라

def min_max(nums):
    nums.sort()

    del nums[0]
    del nums[-1]

T = int(input())

for t in range(T):
    nums = list(map(int,input().strip(' ').split(' ')))

    min_max(nums)
    avg = sum(nums)/len(nums)

    print("#{} {}".format(t+1,round(avg)))