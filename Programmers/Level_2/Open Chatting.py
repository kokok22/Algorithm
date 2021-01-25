def solution(record):
    ## 딕셔너리로 풀면 될 듯
    ## key를 고유키로 만들고 value에 닉네임 넣기

    id_dict = dict()
    answer = []

    for log in record:
        log = log.split(' ')
        if log[0] == 'Leave':
            answer.append([log[1], "님이 나갔습니다."])
            continue

        elif log[0] == 'Enter':
            answer.append([log[1], "님이 들어왔습니다."])

        id_dict[log[1]] = log[2]

    result = []

    for ans in answer:
        result.append("{}".format(id_dict[ans[0]]) + ans[1])

    return result