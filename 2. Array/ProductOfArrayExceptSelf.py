## 배열을 입력받아 output[i]가 자신을 제외한 나머지 모든 요소의 곱셈 결과가 되도록 출력하라
## 단, 나눗셈을 하지 않고 O(n)에 풀어야 한다.


def prodcutExceptSelf(nums):
    # two point를 활용하여 문제를 풀어본다.
    out = []
    p = 1

    # 왼쪽 곱셈
    for i in range(len(nums)):
        out.append(p)
        p *= nums[i]

    p = 1

    # 왼쪽 곱셈 결과에 오른쪽 값을 차례대로 곱셈
    for i in range(len(nums)-1, -1, -1):
        out[i] *= p
        p *= nums[i]

    return out


if __name__ == "__main__":
    nums = [1,2,3,4]
    print(prodcutExceptSelf(nums))