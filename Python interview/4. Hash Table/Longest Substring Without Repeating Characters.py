## 중복 문자가 없는 가장 긴 부분 문자열의 길이를 리턴한다.


def lengthOfLongestSubString(s):
    result = []
    stack = []

    for word in s:
        if not word in stack:
            stack.append(word)
        else:
            result.append(len(stack))
            stack = []
            stack.append(word)


    return max(result)

if __name__ == "__main__":
    s1 = "abcabcbb"
    s2 = "bbbbb"
    s3 = "pwwkew"

    print(lengthOfLongestSubString(s1))
    print(lengthOfLongestSubString(s2))
    print(lengthOfLongestSubString(s3))
