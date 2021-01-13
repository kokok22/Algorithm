## k번 이상 등장하는 요소를 추출하라

def topK(nums, k):
    count = dict()
    result = []

    for key in set(nums):
        count[key] = 0

    for num in nums:
        count[num] += 1

    for key, value in count.items():
        if value >= 2:
            result.append(key)

    return result


if __name__ == "__main__":
    nums = [1,1,1,2,2,3]
    k = 2

    print(topK(nums, k))