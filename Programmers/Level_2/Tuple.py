def solution(s):
    stack = []
    num = []
    answer = []

    strs = ''
    for idx, char in enumerate(s):
        if char.isdigit():
            strs += str(char)

        elif stack and stack[-1] == "{" and char == "}":
            stack.pop()
            num.append(strs)
            answer.append(num)
            strs = ''
            num = []

        elif char == "{" or stack[-1] == "}":
            stack.append(char)

        elif char == ',':
            if not s[idx - 1] == "}":
                num.append(strs)
                strs = ''

    answer = sorted(answer[:-1], key=lambda x: len(x))

    result = []
    for ans in answer:
        for i in ans:
            if not int(i) in result:
                result.append(int(i))

    return result
