## 시와 분으로 이루어진 두개의 시간을 더하라


T = int(input())

for t in range(T):
    time_list = list(map(int,input().strip(' ').split(' ')))

    hour = time_list[0]+time_list[2]
    minute = time_list[1]+time_list[3]

    rnd = minute//60
    minute = minute%60

    hour += rnd
    hour %= 12

    if hour == 0:
        hour = 12

    print("#{} {} {}".format(t+1, hour, minute))