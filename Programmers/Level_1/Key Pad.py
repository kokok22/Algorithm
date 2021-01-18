def solution(numbers, hand):
    pad = [[1, 2, 3],
           [4, 5, 6],
           [7, 8, 9]]

    left = [3, 0]
    right = [3, 2]

    result = ''

    for number in numbers:
        if number == 0:
            place = [3, 1]
        else:
            temp = (number - 1) // 3
            idx = pad[temp].index(number)
            place = [temp, idx]

        if number in [1,4,7]:
            result += 'L'
            left = place
        elif number in [3,6,9]:
            result += 'R'
            right = place
        else:
            l = abs(left[0] - place[0]) + abs(left[1] - place[1])
            r = abs(right[0] - place[0]) + abs(right[1] - place[1])

            if l > r:
                result += 'R'
                right = place
            elif r > l:
                result += 'L'
                left = place
            else:
                if hand == 'right':
                    result += 'R'
                    right = place
                else:
                    result += 'L'
                    left = place

    return result

print([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right")
print(solution([1, 3, 4, 5, 8, 2, 1, 4, 5, 9, 5],"right"))
print("LRLLLRLLRRL")