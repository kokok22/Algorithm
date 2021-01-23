def solution(arr):
    answer = [0, 0]
    new_arr = []
    for ar in arr:
        new_arr += ar

    def recursive(arr):
        n = len(arr)
        half = n ** 0.5

        # 전부 1인 경우
        if sum(arr) == n:
            answer[1] += 1
            return

        # 전부 0인 경우
        elif sum(arr) == 0:
            answer[0] += 1
            return

        # 이도저도 아닌 경우
        temp1, temp2, temp3, temp4 = [], [], [], []
        for i in range(n // 2):
            if i % half < half // 2:
                temp1.append(arr[i])
            else:
                temp2.append(arr[i])

        for i in range(n // 2, n):
            if i % half < half // 2:
                temp3.append(arr[i])
            else:
                temp4.append(arr[i])

        recursive(temp1)
        recursive(temp2)
        recursive(temp3)
        recursive(temp4)

    recursive(new_arr)

    return answer