def solution(cacheSize, cities):
    CACHE = []
    time = 0
    for city in cities:
        city = city.lower()
        if city not in CACHE:
            time += 5
            CACHE.append(city)
            if len(CACHE) == cacheSize + 1:
                CACHE = CACHE[1:]
        else:
            time += 1
            idx = CACHE.index(city)
            CACHE = CACHE[:idx] + CACHE[idx + 1:]
            CACHE.append(city)

    return time

print(solution(3, ["Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul", "Jeju", "Pangyo", "Seoul"]))