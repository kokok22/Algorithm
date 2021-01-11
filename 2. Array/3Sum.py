## 배열을 입력받아 합으로 0을 만들 수 있는 3개의 엘리먼트를 출력하라


# brute force방법으로 푼 것
# def threeSum(nums):
#     result = []
#
#     for idx, num in enumerate(nums):
#         for idx2, pivot in enumerate(nums[idx+1:]):
#             if 0-(num+pivot) in nums[idx+idx2+2:]:
#                result.append([num,pivot,0-(num+pivot)])
#
#     return result


def threeSum(nums):
    result = []
    nums.sort()

    # pivot을 설정
    for i in range(len(nums)-2):
        if i > 0 and nums[i] == nums[i-1]:
            continue

        # 간격을 좁혀가며 합 sum 계산
        left, right = i+1, len(nums)-1
        while left < right:
            sum = nums[i] + nums[left]+nums[right]
            # 조금 더 큰 수를 더해준다.
            if sum < 0:
                left += 1
            # 조금 더 작은 수를 더해준다.
            elif sum > 0:
                right -= 1
            # 0이라면 리스트에 추가해준다.
            else:
                # sum = 0 인 경우이므로 정답 및 스킵 처리
                result.append((nums[i], nums[left], nums[right]))

                # 똑같은 값들은 건너뛰는 작업이다.
                while left < right and nums[left] == nums[left + 1]:
                    left += 1
                while left < right and nums[right] == nums[right - 1]:
                    right -= 1

                left += 1
                right -= 1

    return result

if __name__ == "__main__":
    nums = [-1, 0, 1, 2, -1, -4]
    print(threeSum(nums))