def solution(s):
    strs = s.split(' ')
    answer = []

    for s in strs:
        if not s:
            answer.append('')
            continue
        a = s[0]
        if s[0].isalpha():
            a = s[0].upper()

        for char in s[1:]:
            if char.isalpha():
                a += char.lower()
            else:
                a += char

        answer.append(a)

    return ' '.join(answer)

print(solution("hello    world"))