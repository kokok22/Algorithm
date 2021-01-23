def solution(numbers, target):
    sum_list = [numbers[0], -numbers[0]]

    for num in numbers[1:]:
        temp = []
        for total in sum_list:
            temp.append(total + num)
            temp.append(total - num)

        sum_list = temp

    return sum_list.count(target)