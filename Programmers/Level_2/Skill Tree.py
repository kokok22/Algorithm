# for - else : break로 종료되지 않으면 else문이 실행된다.

def solution(skill, skill_trees):
    answer = 0

    for skills in skill_trees:
        skill_list = list(skill)

        for s in skills:
            if s in skill:
                if s != skill_list.pop(0):
                    break
        else:
            answer += 1

    return answer

# def solution(skill, skill_trees):
#     count = 0
#
#     for skill_tree in skill_trees:
#         temp = ''
#         for char in skill_tree:
#             if char in skill:
#                 temp += char
#
#         idx = 0
#         flag = True
#
#         while idx < len(temp):
#             if temp[idx] != skill[idx]:
#                 flag = False
#                 break
#             else:
#                 idx += 1
#
#         if flag:
#             count += 1
#
#     return count


print(solution("CBD", ["BACDE", "CBADF", "AECB", "BDA"]))