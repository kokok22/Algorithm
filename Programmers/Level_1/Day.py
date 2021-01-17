def solution(a, b):
    days = ['SUN', 'MON', 'TUE', 'WED', 'THU', 'FRI', 'SAT']
    months = ['FRI', 'MON', 'TUE', 'FRI', 'SUN',
              'WED', 'FRI', 'MON', 'THU', 'SAT',
              'TUE', 'THU']

    idx = (b-1) % 7
    month = months[a-1]

    idx += days.index(month)

    answer = days[idx % 7]

    return answer

print(solution(12,1))