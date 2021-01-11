## 높이를 입력받아 비 온 후 얼마나 많은 물이 쌓일 수 있는지 계산하라.

def trap(height):
    if not height:
        return 0

    volume = 0
    left, right = 0, len(height)-1

    left_max, right_max = height[left], height[right]

    while left < right:
        left_max, right_max = max(height[left], left_max),\
                                max(height[right], right_max)

        # 더 높은 쪽을 향해 투 포인터 이동
        # 가장 높은 곳을 기준으로 나뉘게 되는 것이다.
        if left_max <= right_max:
            volume += left_max - height[left]
            left += 1
        else:
            volume += right_max - height[right]
            right -= 1

    return volume

if __name__ == "__main__":
    height = [0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1]

    print(trap(height))