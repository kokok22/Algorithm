## 패턴 마디의 길이
## (문제가 별로임....)

def checkDuplicate(words):
    size = 1
    result = words[:size]
    check = True

    while True:
        if size > 10:
            return 0
        for i in range(size,len(words),size):
            if result == words[i:i+size]:
                check = True
                continue

            elif i+size < len(words):
                size += 1
                result = words[:size]
                check = False
                break

        if check == True:
            return len(result)


T = int(input())

for i in range(T):
    words = input()
    print("#{} {}".format(i+1,checkDuplicate(words)))