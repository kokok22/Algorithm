def solution(n):
    num = bin(n).count('1')

    # 2배이면 어차피 모두 왼쪽으로 한칸씩 이동하는 것
    for i in range(n + 1, 2 * n + 1):
        if bin(i).count('1') == num:
            return i