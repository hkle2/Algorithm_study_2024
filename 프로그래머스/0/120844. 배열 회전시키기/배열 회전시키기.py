def solution(numbers, direction):
    answer = [0 for i in range(len(numbers))]
    if direction == "right":
        for i in range(len(numbers)-1):
            answer[i + 1] = numbers[i]
        answer[0] = numbers[-1]
    else:
        for i in range(len(numbers)-1):
            answer[i] = numbers[i + 1]
        answer[-1] = numbers[0]
    return answer