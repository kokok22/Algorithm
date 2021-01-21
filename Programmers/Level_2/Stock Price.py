def solution(prices):
    answer = [0]*len(prices)
    stack = [[prices[0],0]]

    for idx, price in enumerate(prices[1:]):
        while True:
            if stack and stack[-1][0] > price:
                temp = stack.pop()
                answer[temp[1]] = idx+1-temp[1]
            else:
                stack.append([price,idx+1])
                break

    while stack:
        temp = stack.pop()
        answer[temp[1]] = len(prices)-temp[1]-1

    return answer

print(solution([2,1]))