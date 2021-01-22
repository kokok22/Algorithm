def letterCombinations(digits):
    def dfs(index, path):
        # 끝까지 탐색하면 백트래킹
        if len(path) == len(digits):
            result.append(path)
            return


        for i in range(index, len(digits)):
            # 숫자에 해당하는 모든 문자열 반복
            for j in dic[digits[i]]:
                dfs(i+1, path+j)

    if not digits:
        return []

    dic = {"2" : "abc", "3" : "def", "4" : "ghi", "5" : "jkl",
           "6" : "mno", "7" : "pqrs", "8" : "tuv", "9" : "wxyz"}
    result = []
    dfs(0,"")

    return result

print(letterCombinations("23"))