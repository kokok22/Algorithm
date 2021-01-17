def solution(arr):
    answer = []
    pre = -1

    for ar in arr:
        if ar != pre:
            answer.append(ar)
            pre = ar

    return answer