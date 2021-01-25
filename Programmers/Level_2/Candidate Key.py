from itertools import combinations


# 기존에 사용된 조합인지 확인
def pre(op, stacks):
    for stack in stacks:
        stack
        flag = True
        for s in stack:
            if s in op:
                print(s, op, flag)
            else:
                print(s, op, flag)
                flag = False
        if flag:
            return False
    return True


# 개인키인지 확인
def check(tup):
    return len(tup) == len(set(tup))


def solution(relation):
    num = len(relation[0])
    order = [i for i in range(num)]
    count = 0

    stack = []

    i = 0
    while i <= len(order):
        i += 1
        # 후보키가 가능한 조합을 생성한다.
        check_list = list(combinations(order, i))

        for chk in check_list:
            # 최소성 만족 확인
            if pre(chk, stack):

                # value 추출
                temp_list = []
                for j in range(len(relation)):
                    temp_str = ""
                    for p in chk:
                        temp_str += relation[j][p]
                    temp_list.append(temp_str)

                # 후보키 여부 확인
                if check(temp_list):
                    count += 1
                    stack.append(chk)

    return count