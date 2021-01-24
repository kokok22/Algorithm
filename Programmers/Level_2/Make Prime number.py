from itertools import combinations

def solution(nums):
    num_list = list(combinations(nums, 3))
    sum_list = []

    for num in num_list:
        sum_list.append(sum(num))

    cnt = 0

    for num in sum_list:
        if num % 2 == 0:
            continue
        flag = True

        for i in range(3, int(num ** 0.5) + 1, 2):
            if num % i == 0:
                flag = False
                break
        if flag:
            cnt += 1

    return cnt

print(solution([1,2,7,6,4]))