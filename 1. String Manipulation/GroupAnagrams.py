## 문자열 배열을 받아 애너그램 단위로 그룹핑하라
## 애너그램이란? 문자를 재배열하여 다른 뜻을 가진 단어로 바꾸는 것을 말한다.


def groupAnagrams(words):
    group = dict()

    # 단어를 sorting하게 된다면 같은 문자로 구성된 경우 같은 값이 나오게 된다.
    # 그렇게 나온 값을 key로 dict에 단어들을 저장한다면 애너그램끼리 묶이게 된다.
    for word in words:
        key = ''.join(sorted(word))
        if key in group:
            group[key].append(word)
        else:
            group[key] = [word]

    return group.values()


if __name__ == "__main__":
    strs = ["eat", "tea", "tan", "ate", "nat", "bat"]

    print("input : \n {}".format(strs))
    print("output : \n {}".format(groupAnagrams(strs)))