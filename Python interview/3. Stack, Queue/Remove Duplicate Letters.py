## 중복된 문자를 제외하고 사전식 순서로 나열하라

def removeDuplicateLetter(s):
    # 사전식 순서란 사전에서 가장 먼저 찾을 수 있는 단어로
    # 모든 문자가 사용되어야 하며 뒤에 중복되어 나타난다면
    # 둘중에 하나를 택 할 수 있다.
    # ebcabc -> eabc

    # 전체 집합을 정렬한 다음 알파벳 순서로 꺼내기
    for char in sorted(set(s)):
        # 실제에서 해당 알파벳 뒤에 있는 문자열 추출
        suffix = s[s.index(char):]

        # 나와야 되는 문자가 현재 suffix에 다 포함 되어 있는지 확인
        # 없으면 다른 애가 먼저 꺼내져야 하기 때문.
        if set(s) == set(suffix):
            return char + removeDuplicateLetter(suffix.replace(char, ''))
    return ''


if __name__=="__main__":
    s1 = 'bcabc'
    s2 = 'cbacdcbc'

    print(removeDuplicateLetter(s1))
    print(removeDuplicateLetter(s2))
