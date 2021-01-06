## 로그를 재 정렬하라.
## 1. 로그의 가장 앞 부분은 식별자다.
## 2. 문자로 구성된 로그가 숫자 로그보다 앞에 온다.
## 3. 식별자는 순서에 영향을 끼치지 않지만, 문자가 동일할 경우 식별자 순으로 한다.
## 4. 숫자 로그는 입력순서대로 한다.


def reorderLogFiles(logs):
    letter = []
    digit = []

    for log in logs:
        if log.split()[1].isdigit():
            digit.append(log)
        else:
            letter.append(log)

    # 2가지 조건을 key로 쓰고 싶으면 lambda를 쓰자
    # 첫번째 조건이 같으면 두번째 조건을 비교
    # '-'를 붙이면 내림차순으로 정렬
    letter.sort(key=lambda x : (x.split()[1:],x.split()[0]))

    return letter+digit


if __name__ == "__main__":
    logs = ["dig1 8 1 5 1", "let1 art can", "dig2 3 6", "let2 own kit dig", "let3 art zero"]

    print("1. \tinput : {}".format(logs))
    print("\toutput : {}".format(reorderLogFiles(logs)))