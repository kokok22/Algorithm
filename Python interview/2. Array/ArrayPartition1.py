## n개의 페어를 이용한 min(a,b)의 합으로 만들 수 있는 가장 큰 수를 출력하라.

def arrayPairSum(nums):
    # min의 합이 최대가 되기 위해서는 최대한 많은 수의 pair가 생겨야 한다.
    return sum(sorted(nums)[::2])


if __name__ == "__main__":
    nums = [1,4,3,2]
    print(arrayPairSum(nums))