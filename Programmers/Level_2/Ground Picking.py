def solution(land):
    map = land[0]

    for line in land[1:]:
        temp = []
        for idx, char in enumerate(line):
            num = max(map[:idx] + map[idx + 1:])
            temp.append(num + char)
        map = temp

    return max(map)

print(solution([[1,2,3,5],[5,6,7,8],[4,3,2,1]]	))