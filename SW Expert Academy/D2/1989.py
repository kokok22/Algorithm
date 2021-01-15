## palindrome

def isPalindrome(word):
    return word == word[::-1]


T = int(input())

for t in range(T):
    word = input()

    print("#{} {}".format(t+1,int(isPalindrome(word))))