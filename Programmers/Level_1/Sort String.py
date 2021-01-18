def solution(strs):
    up = []
    low = []

    for s in strs:
        if s.islower():
            low.append(s)
        else:
            up.append(s)

    up.sort(reverse=True)
    low.sort(reverse=True)

    return ''.join(low+up)

print(solution("Zbacedgf"))