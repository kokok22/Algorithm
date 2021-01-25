def solution(str1, str2):
    stack1 = []
    stack2 = []

    for i in range(len(str1) - 1):
        if str1[i].isalpha() and str1[i + 1].isalpha():
            stack1.append(str1[i:i + 2].lower())

    for i in range(len(str2) - 1):
        if str2[i].isalpha() and str2[i + 1].isalpha():
            stack2.append(str2[i:i + 2].lower())

    inter = []
    union = stack2.copy()

    for i in range(len(stack1)):
        if stack1[i] in stack2:
            inter.append(stack1[i])
            stack2[stack2.index(stack1[i])] = 0
        else:
            union.append(stack1[i])

    if inter or union:
        answer = len(inter) / len(union)
    else:
        answer = 1

    return int(answer * 65536)