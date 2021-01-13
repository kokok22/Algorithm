## 중복된 문자를 제외하고 사전식 순서로 나열하라

def removeDuplicateLetter(strs):
    # 사전식 순서란 사전에서 가장 먼저 찾을 수 있는 단어로
    # 모든 문자가 사용되어야 하며 뒤에 중복되어 나타난다면
    # 둘중에 하나를 택 할 수 있다.
    # ebcabc -> eabc

    result = []

    return result


if __name__=="__main__":
    s1 = 'bcabc'
    s2 = 'cbacdcbc'

    print(removeDuplicateLetter(s1))
    print(removeDuplicateLetter(s2))
