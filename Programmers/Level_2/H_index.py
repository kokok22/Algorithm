def solution(citations):
    hindex = [0] * (len(citations) + 1)
    h = 1

    for i in range(len(citations)):
        cnt = 0

        for citation in citations:
            if h <= citation:
                cnt += 1

        if h <= cnt:
            hindex[h] = h
        h += 1

    return max(hindex)

print(solution([3, 0, 6, 1, 5]))