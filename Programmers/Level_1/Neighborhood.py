def solution(n, lost, reserve):
    student = [1] * n

    for l in lost:
        student[l - 1] -= 1
    for res in reserve:
        student[res - 1] += 1

    num = student.count(2)
    while num:
        idx = student.index(2)

        if idx > 0 and student[idx - 1] == 0:
            student[idx - 1] = 1
        elif idx < n - 1 and student[idx + 1] == 0:
            student[idx + 1] = 1

        student[idx] = 1
        num -= 1

    answer = n - student.count(0)

    return answer

print(solution(	5, [2, 4], [1, 3, 5]))