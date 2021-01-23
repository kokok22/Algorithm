## 투 포인터로 움직이는 것이 할당하는 것보다 더 빠르다.
## 다시 할당하고 하는 방법 쓰지 말자

def solution(people, limit):
    answer = 0
    people.sort()

    f_cnt =0
    e_cnt =len(people)-1
    while e_cnt - f_cnt >=1:
        if people[f_cnt] +people[e_cnt] <= limit:
            f_cnt +=1
            e_cnt -=1
        else:
            e_cnt -=1
        answer +=1
    if e_cnt == f_cnt:
        answer +=1
    return answer

#
# def solution(people, limit):
#     people.sort(reverse=True)
#
#     count = 0
#     while people:
#
#         if people[0] <= limit // 2:
#             if len(people) % 2 == 0:
#                 count += len(people) // 2
#                 break
#             else:
#                 count += len(people) // 2 + 1
#                 break
#
#         if people[0] + people[-1] <= limit:
#             count += 1
#             people = people[1:-1]
#         else:
#             people = people[1:]
#             count += 1
#
#     return count