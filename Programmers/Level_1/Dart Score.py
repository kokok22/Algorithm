def solution(dartResult):
    answer = [0, ]

    while dartResult:
        score = int(dartResult[0])

        if dartResult[1] == '0':
            score = int(dartResult[0:2])
            dartResult = dartResult[1:]

        bonus = int(dartResult[1].replace("S", '1').replace("D", '2').replace("T", '3'))
        option = 1
        dartResult = dartResult[2:]

        if dartResult and (dartResult[0] == "*" or dartResult[0] == "#"):
            option = int(dartResult[0].replace("*", '2').replace("#", '-1'))
            dartResult = dartResult[1:]

        if option == 2:
            answer[-1] *= option

        answer.append((score ** bonus) * option)

    return sum(answer)

print(solution("1S2D*3T"))
print(solution("1D2S#10S"))