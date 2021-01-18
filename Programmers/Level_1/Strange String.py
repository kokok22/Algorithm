def solution(s):
    s_list = s.split(' ')

    answer = ''

    for word in s_list:
        for idx, char in enumerate(word):
            if idx%2 == 0:
                answer += char.upper()
            else:
                answer += char.lower()

        if not len(s) == len(answer):
            answer += ' '

    return answer

print(solution("try hello world"))