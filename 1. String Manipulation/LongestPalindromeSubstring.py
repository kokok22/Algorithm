## 가장 긴 팰린드롬 부분 문자열을 출력하라


def longest_palindrome_substring(s):
    def expand(left, right):
        while left >= 0 and right <= len(s) and s[left] == s[right-1]:
            left -= 1
            right += 1

        return s[left+1 : right-1]

    if len(s) < 2 or s == s[::-1]:
        return s

    result = ''

    for i in range(len(s)-1):
        result = max(result,
                     expand(i,i+1),
                     expand(i,i+2),
                     key=len)

    return result

if __name__ == "__main__":
    str1 = "babad"
    str2 = "helfmslmepmmilimmpemleoiwpm"


    print("{}'s LPS is {}".format(str1, longest_palindrome_substring(str1)))
    print("{}'s LPS is {}".format(str2, longest_palindrome_substring(str2)))
