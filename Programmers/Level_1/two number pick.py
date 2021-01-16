def solution(numbers):
    answer = []

    for idx, num1 in enumerate(numbers):
        for num2 in numbers[idx + 1:]:
            answer.append(num1 + num2)

    return sorted(list(set(answer)))