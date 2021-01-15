## 괄호로 된 입력값이 올바른지 판별하라.

def isValid(s):
    stack = []
    table = {
        ')' : '(',
        '}' : '{',
        ']' : '[',
    }

    for char in s:
        # 닫는 기호가 아니라면 stack에 넣는다.
        if char not in table:
            stack.append(char)
        # stack이 비었거나 stack에서 pop된 문자가 char의 value가 아니라면 false
        elif not stack or table[char] != stack.pop():
            return False

    # s가 다 끝났는데 stack에 문자가 남아있다면 괄호가 잘못 쳐져 있는 것이다.
    return len(stack) == 0


if __name__ =="__main__":
    s = '(){}[]'
    print(isValid(s))