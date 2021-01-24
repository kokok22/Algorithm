def solution(n):
    answer = [i for i in range(1, n // 2 + 1)]
    idx = 0
    count = 1

    f_idx = len(answer)

    while answer[0] <= n:
        idx += 1
        for i in range(0, f_idx):
            answer[i] += i + idx + 1
            if answer[i] == n:
                count += 1
            if answer[i] > n:
                f_idx = i
                break

    return count

print(solution(15))