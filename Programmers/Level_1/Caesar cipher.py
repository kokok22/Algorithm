def solution(s, n):
    answer = ''
    for char in s:
        new = ord(char)
        if char.isupper():
            if new + n > ord('Z'):
                char = chr(ord('A') + (new + n - ord('Z')) - 1)
            else:
                char = chr(new + n)

        elif char.islower():
            if new + n > ord('z'):
                char = chr(ord('a') + (new + n - ord('z')) - 1)
            else:
                char = chr(new + n)

        answer += char

    return answer