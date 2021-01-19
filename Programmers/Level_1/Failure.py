def solution(N, stages):
    total = []

    stages.sort()

    for idx in range(1, N + 1):
        num = stages.count(idx)
        if num:
            fail = num / len(stages[stages.index(idx):])
        else:
            fail = 0
        total.append([idx, fail])

    answer = sorted(total, key=lambda x : (-x[1],x[0]))

    return [i[0] for i in answer]

print(solution(5, [2, 1, 2, 6, 2, 4, 3, 3]))