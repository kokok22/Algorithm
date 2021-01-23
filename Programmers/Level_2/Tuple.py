## strip으로 안쓰는 문자열 제거
## split으로 분리해줌
## 똑똑한 방법

def solution(s):
    s = s.lstrip('{').rstrip('}').split('},{')

    result = []
    for i in s:
        result.append(i.split(','))

    result.sort(key=lambda a: len(a))

    answer = []
    for num_list in result:
        for number in num_list:
            if not int(number) in answer:
                answer.append(int(number))

    return answer


## 내가 푼 것
## 상당히 귀찮게 풀었음. 경우의 수 다 나눠서 문자열 처리해줌
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
