def solution(files):
    answer = []

    for file in files:
        idx1 = 0
        idx2 = 0
        flag = False
        for i in range(len(file)):
            if (not flag) and file[i].isdigit():
                idx1 = i
                flag = True

            if flag and not (file[i].isdigit()):
                idx2 = i
                break
        else:
            idx2 = len(file)

        answer.append([file[:idx1], file[idx1:idx2], file[idx2:]])

    temp = sorted(answer, key=lambda x: (x[0].lower(), int(x[1])))
    result = []
    for strs in temp:
        result.append(''.join(strs))

    return result

print(solution(["F-5 Freedom Fighter", "B-50 Superfortress", "A-10 Thunderbolt II", "F-14 Tomcat"]))