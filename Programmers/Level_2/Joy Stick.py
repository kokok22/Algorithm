def solution(name):
    alpha = [chr(i) for i in range(65,91)]
    char_list = []

    for char in name:
        idx = alpha.index(char)

        if idx < 26-idx:
            count = idx
        else:
            count = 26-idx

        char_list.append(count)

    # 앞으로 갈지 뒤로 갈지 결정
    check1 = 0
    for char in char_list[1:]:
        if char == 0:
            check1 +=1
        else:
            break

    check2 = 0
    for char in char_list[::-1]:
        if char == 0:
            check2 +=1
        else:
            break


    answer = sum(char_list)+len(char_list)-1-max(check1, check2)
    if answer == -1:
        return 0

    # 앞으로 갔다가 뒤로 가는 경우
    temp = sum(char_list)+len(char_list)-char_list.count(0)+(check1+check2)*2

    if temp < answer:
        answer = temp

    return answer

print(solution("JEROEN"))
print(solution("JAN"))
