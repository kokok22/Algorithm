def solution(n, arr1, arr2):
    answer = []

    for ar1, ar2 in zip(arr1, arr2):
        temp = str(bin(ar1 | ar2))[2:]
        temp = " " * (n - len(temp)) + temp
        temp = temp.replace("1","#").replace("0"," ")
        answer.append(temp)

    return answer



print(solution(5, [9, 20, 28, 18, 11], [30, 1, 21, 17, 28]))