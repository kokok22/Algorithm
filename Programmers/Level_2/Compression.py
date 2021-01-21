# string으로 숫자를 받게 되는 경우 자릿수가 증가되는 경우를 꼭 생각해야 된다!

def solution(s):
    stack = ''
    size = len(s)

    min_length = size

    for i in range(1, size+1):
        answer = ''
        count = 0
        flag = False
        check = [1,0]

        for j in range(0,size,i):
            if stack == s[j:j+i]:
                check[0] += 1
                if not flag:
                    count+=1
                    flag = True
                if check[0] >= 10 and check[1]==0:
                    count += 1
                    check[1] = 1

            else:
                check = [1,0]
                stack = s[j:j+i]
                answer += stack
                flag = False

        if min_length > len(answer)+count:
            min_length = len(answer)+count

    return min_length


print(solution("aabbaccc"))
print(solution("ababcdcdababcdcd"))
print(solution("abcabcdede"))
print(solution("abcabcabcabcdededededede"))
print(solution("xxxxxxxxxxyyy"))

