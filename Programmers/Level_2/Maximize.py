import re

def solution(expression):
    # (*, +, -)
    # (+, *, -)
    # (-, *, +)
    # (+, -, *)
    print(expression)
    num = re.sub('[*\-+]', ' ', expression)

    print(num)

print(solution("100-200*300-500+20"))