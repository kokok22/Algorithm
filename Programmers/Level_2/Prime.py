from itertools import permutations

def prime(num):
    if num == 2 or num ==3:
        return True

    if num <= 1 or num%2==0:
        return False

    n = int(num**0.5)
    for k in range(3, n+1,2):
        if num % k == 0:
            return False

    return True

def solution(numbers):
    answer = 0
    lists = []

    for i in range(1,len(numbers)+1):
        lists += list(permutations(list(numbers), i))

    for i in range(len(lists)):
        lists[i] = int("".join(lists[i]))

    for i in list(set(lists)):
        if prime(i):
            answer += 1

    return answer

print(solution("17"))