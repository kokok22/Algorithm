def solution(numbers):
    numbers = list(map(str,numbers))
    num_list = sorted(numbers, key=lambda x: (x[0:1], int(x[0:2]) % 10 if int(x) > 9 else int(x), \
                                              int(x[0:3]) % 10 if int(x) > 99 else int(x[0]), \
                                              # int(x[0:4]) % 10 if int(x) > 999 else int(x[0]), \
                                              -int(x[-2:])
                                              ), reverse=True)

    answer = ''.join(num_list)

    # 0으로만 된 경우
    if answer.count("0") == len(answer):
        answer = "0"

    return answer

print(solution([6, 10, 2]))
print(solution([3, 30, 34, 5, 9]))
print(solution([10, 101]))
print(solution([1, 11, 111, 1111]))
print(solution([0, 0, 0, 0, 0, 0]))
print(solution([2,20,200]))
print(solution([0,0,70]))
print(solution([0,0,0,1000]))
print(solution([0,0,1000,0]))
print(solution([1000,0,0]))
print(solution([12,121]))
print(solution([21,212]))
print(solution([11, 12, 10]))
print(solution([0,0,0,1]))
print(solution([1,2,3,1,1,3]))
print(solution([1,2,21, 21]))




print('10'[-2:])
print('101'[-2:])
