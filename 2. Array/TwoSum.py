# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자를 리턴하라.

def two_sum(nums, target):
    result = []

    # 두 숫자
    for idx, num in enumerate(nums):
        if target-num in nums[idx+1:]:
            result.append([num,target-num])

    return result


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(two_sum(nums, target))