def solution(p):
    global answer
    answer = ''
    dic = {'(': 1, ')': -1}

    def balanced(p):
        global answer
        stack = []
        count = 0

        if not p:
            return

        # 균형 잡힌 괄호 문자열 구하기
        for idx, char in enumerate(p):
            if stack and stack[-1] == '(' and char == ')':
                stack.pop()
            else:
                stack.append(char)

            count += dic[char]

            # 찾음
            if count == 0:
                # 올바른 괄호 문자열
                if not stack:
                    answer += ''.join(p[:idx + 1])
                    p = p[idx + 1:]
                    return balanced(p)
                # 올바르지 못한 문자열
                else:
                    answer += '('
                    balanced(p[idx + 1:])
                    answer += ')'
                    for char in p[1:idx]:
                        if char == '(':
                            answer += ')'
                        else:
                            answer += '('

                    return

    balanced(p)

    return answer

print(solution(")("))