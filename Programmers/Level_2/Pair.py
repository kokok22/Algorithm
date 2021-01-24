def solution(s):
    if len(s) % 2 == 1:
        return 0

    stack = []
    for char in s:
        if stack and stack[-1] == char:
            stack.pop()
        else:
            stack.append(char)

    if stack:
        return 0
    else:
        return 1

print(solution("baabaa"))