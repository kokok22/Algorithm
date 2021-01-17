def solution(answers):
    answer = [0,0,0]

    one = [1, 2, 3, 4, 5] * 8
    two = [2, 1, 2, 3, 2, 4, 2, 5] * 5
    three = [3, 3, 1, 1, 2, 2, 4, 4, 5, 5] * 4

    pivot = 0

    for ans in answers:
        answer[0] += int(one[pivot] == ans)
        answer[1] += int(two[pivot] == ans)
        answer[2] += int(three[pivot] == ans)
        pivot += 1

        if pivot == 40:
            pivot = 0

    max_num = -1
    idx_list = []

    for idx, i in enumerate(answer):
        if max_num < i:
            max_num = i
            idx_list = []
            idx_list.append(idx + 1)
        elif max_num == i:
            idx_list.append(idx + 1)

    return idx_list

print(solution([1,2,3,4,5]))