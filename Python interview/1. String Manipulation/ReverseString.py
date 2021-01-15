## 문자열을 뒤집는 함수를 작성하라.
## 입력값은 문자 배열이며, 리턴 없이 리스트 내부를 직접 조작하라

def reverseString(s):
    ## 파이썬스럽게 푸는 법
    s.reverse()
    return s

    ## 투 포인트를 이용한 스왑
    # start = 0
    # end = len(s)-1
    #
    # while start < end:
    #     s[start], s[end] = s[end], s[start]
    #     start += 1
    #     end -= 1
    #
    # return s


if __name__ == "__main__":
    str1 = ["h", "e", "l", "l", "o"]
    str2 = ["H", "a", "n", "n", "a", "h"]

    print("--ReverseString--")
    print("1. \tinput : {}".format(str1))
    print("\toutput : {}".format(reverseString(str1)))

    print("2. \tinput : {}".format(str2))
    print("\toutput : {}".format(reverseString(str2)))

