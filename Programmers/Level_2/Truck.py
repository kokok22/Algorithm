def solution(bridge_length, weight, truck_weights):
    time = []        # 경과 시간
    passing = []    # 지나가는 중
    count = 0


    while truck_weights or passing:
        count +=1
        for idx, t in enumerate(time):
            time[idx] +=1

        if time and time[0]>bridge_length:
            time.pop(0)
            passing.pop(0)

        if truck_weights and weight >= sum(passing)+truck_weights[0]:
            passing.append(truck_weights[0])
            truck_weights.pop(0)
            time.append(1)

    return count


print(solution(2,10,[7,4,5,6]))