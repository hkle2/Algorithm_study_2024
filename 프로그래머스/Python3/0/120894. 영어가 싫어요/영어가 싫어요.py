def solution(numbers):
    answer = 0
    num = []
    l = ["zero", "one", "two", "three", "four", "five", "six", "seven", "eight", "nine"]
    for i in range(len(numbers)):
        for j in range(3, 6):
            if numbers[i:i+j] in l:
                num.append(str(l.index(numbers[i:i+j])))
                break
    answer = "".join(num)
    return int(answer)