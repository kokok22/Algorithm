## 가장 원점과 가까운 거리와 개수

T = int(input())

for t in range(T):
    size = int(input())

    distance = list(map(int, input().strip(' ').split(' ')))
    distance = [abs(i) for i in distance]
    distance.sort()

    min_value = min(distance)
    total = distance.count(min_value)

    print("#{} {} {}".format(t+1, min_value, total))