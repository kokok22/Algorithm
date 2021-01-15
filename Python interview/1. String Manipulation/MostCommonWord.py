## 금지된 단어를 제외한 가장 흔하게 등장하는 단어를 출력하라.
## 대소문자 구분을 하지 않으며, 구두점(쉼표, 마침표 등) 또한 무시한다.

import re

def most_common_word(paragraph, banned=None):
    freq_word = [0,None]

    # 특수문자제거 -> 소문자로 변경 -> 띄어쓰기 기준 분리
    words = re.sub(r'[^\w]', ' ', paragraph).lower().split()

    for word in words:
        if freq_word[0] < words.count(word) and banned[0] != word:
            freq_word[1] = word
            freq_word[0] = words.count(word)

    return freq_word[1]


if __name__ == "__main__":
    paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
    banned = ["hit"]

    print("input : {}".format(paragraph))
    print("most common word is {}".format(most_common_word(paragraph, banned)))