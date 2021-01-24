def solution(n, words):
    stack = []

    pre = None
    for idx, word in enumerate(words):
        if pre and (word in stack or pre != word[0]):
            cycle = (idx) // n + 1
            no = (idx) % n + 1

            return [no, cycle]

        else:
            stack.append(word)
            pre = word[-1]

    return [0, 0]

print(solution(3,["hello", "observe", "effect", "take", "either",
                "recognize", "encourage", "ensure", "establish",
                "hang", "gather", "refer", "reference", "estimate", "executive"]))