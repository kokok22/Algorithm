def solution(progresses, speeds):
    answer = []
    time = 0
    count = 0
    while len(progresses)> 0:
        if (progresses[0] + time*speeds[0]) >= 100:
            progresses.pop(0)
            speeds.pop(0)
            count += 1
        else:
            if count > 0:
                answer.append(count)
                count = 0
            time += 1
    answer.append(count)
    return answer


# def solution(progresses, speeds):
#     answer = []
#     queue = []
#     pivot = 0
#     size = len(speeds)
#
#     while pivot != size:
#         for idx, speed in enumerate(speeds):
#             if progresses[idx] < 100:
#                 progresses[idx] += speed
#
#             elif progresses[idx] >= 100:
#                 queue.append(idx)
#                 progresses[idx] = 0
#                 speeds[idx] = 0
#
#         count = 0
#         while pivot in queue:
#             del queue[queue.index(pivot)]
#             count += 1
#             pivot += 1
#
#         if count:
#             answer.append(count)
#
#     return answer

print(solution([95, 90, 99, 99, 80, 99], [1, 1, 1, 1, 1, 1]))