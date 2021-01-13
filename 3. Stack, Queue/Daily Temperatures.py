## 매일의 화씨 온도(F) 리스트 T를 입력받아서, 더 따뜻한 날씨를 위해서는
## 며칠을 더 기다려야 하는지를 출력하라

def dailyTemperature(t):
    answer = [0]*len(t)
    stack = []

    for i, cur in enumerate(t):
        # 현재 온도가 stack보다 높다면 정답 처리
        # stack에 값을 넣는 것이 아니라 idx를 넣어서 계산이 가능하다.
        while stack and cur > t[stack[-1]]:
            last = stack.pop()
            answer[last] = i-last
        stack.append(i)

    return answer


if __name__ == "__main__":
    T = [73, 74, 75, 71, 69, 72, 76, 73]
    print(dailyTemperature(T))