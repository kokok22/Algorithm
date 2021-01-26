def solution(msg):
    cache = [chr(i) for i in range(65, 91)]
    answer = []
    cnt = 1
    idx = 0
    while idx < len(msg):
        p = 2
        while True:
            cnt += 1

            if msg[idx:idx + p] in cache:
                if idx + p >= len(msg):
                    answer.append(cache.index(msg[idx:idx + p]) + 1)
                    p += 1
                    break
                p += 1


            else:
                answer.append(cache.index(msg[idx:idx + p - 1]) + 1)
                cache.append(msg[idx:idx + p])
                break
        idx += (p - 1)

    return answer