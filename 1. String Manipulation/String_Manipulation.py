import re


## 1.주어진 문자열이 팬린드롬(앞뒤가 똑같은 단어)인지 확인하라.
##   대소문자를 구분하지 않으며, 영문자와 숫자만을 대상으로 한다.
def isPalindrome(s):
    s = re.sub('[^\w]', '',s).lower()

    return s == s[::-1]




if __name__ == "__main__":
    # first
    str1 = "A man, a plan, a canal: Panama"
    str2 = "race a car"
    str3 = "hello world"
    print("--isPalidrome--")
    print("1. {} is palidrome? {}".format(str1, isPalindrome(str1)))
    print("2. {} is palidrome? {}".format(str2, isPalindrome(str2)))
    print("3. {} is palidrome? {}".format(str3, isPalindrome(str3)))
    print()


    # second
