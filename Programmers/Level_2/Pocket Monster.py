def solution(nums):
    num_set = set(nums)
    return min(len(num_set), len(nums)//2)

print(solution([3,3,3,2,2,4]))