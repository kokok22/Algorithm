# 덧셈하여 타겟을 만들 수 있는 배열의 두 숫자를 리턴하라.

def two_sum(nums, target):
    result = []

    nums_map = {}
    # 키와 값을 바꾸어 딕셔너리로 저장
    for i, num in enumerate(nums):
        nums_map[num] = i

    # 타겟에서 첫 번째 수를 뺀 결과를 키로 조회
    for i, num in enumerate(nums):
        if target-num in nums_map and i != nums_map[target-num]:
            result.append([nums.index(num), nums_map[target-num]])

    return result


if __name__ == "__main__":
    nums = [2, 7, 11, 15]
    target = 9

    print(two_sum(nums, target))