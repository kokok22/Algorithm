def solution(s):
    answer = 0
    count = 0

    while s != '1':
        count += 1
        l = len(s)
        cnt = s.count('1')
        answer += l - cnt
        s = bin(cnt)[2:]

    return [count, answer]

print(solution("110010101001"))