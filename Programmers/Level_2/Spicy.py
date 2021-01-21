import heapq

# sorting을 계속해줘야 하는 경우에 사용하면 좋을 것 같다.
def solution(scoville, K):
    heapq.heapify(scoville)

    count = 0
    while True:
        if scoville[0] > K:
            break
        elif len(scoville) < 2:
            return -1

        one = heapq.heappop(scoville)
        two = heapq.heappop(scoville)

        new = one + (two*2)

        heapq.heappush(scoville, new)

        count += 1
    return count

print(solution([1, 5, 3, 12, 10, 3]	,10))
