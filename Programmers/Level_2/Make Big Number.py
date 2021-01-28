def solution(number, k):
    answer = []
    size = len(number) - k

    for i in range(size):
        max_num = '0'
        idx = 0
        for j in range(k + 1):
            if max_num < number[j]:
                max_num = number[j]
                idx = j
                if max_num == '9':
                    break

        answer.append(max_num)
        number = number[idx+1:]
        k -= idx

    return ''.join(answer)

print(solution("4177252841", 4))