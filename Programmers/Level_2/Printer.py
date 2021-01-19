def solution(priorities, location):
    answer = []
    temp = []

    for idx, i in enumerate(priorities):
        temp.append([idx,i])

    max_num = max(temp,key=lambda a:a[1])
    num = temp.pop(0)

    while temp:
        if num[1] < max_num[1]:
            temp.append(num)
        else:
            answer.append(num)
            max_num = max(temp,key=lambda a:a[1])

        num = temp.pop(0)

    answer.append(num)

    idx = answer.index([location,priorities[location]])

    return idx+1


print(solution([2, 1, 3, 2],2))
print(solution([1, 1, 9, 1, 1, 1],0))