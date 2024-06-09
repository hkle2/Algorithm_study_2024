def solution(bin1, bin2):
    answer1 = 0
    answer2 = 0
    for i, j in enumerate(bin1[::-1]):
        answer1 += 2**int(i) * int(j)
    for i, j in enumerate(bin2[::-1]):
        answer2 += 2**int(i) * int(j)
    answer = bin(answer1 + answer2)[2:]
    return answer

def solution(bin1, bin2):
    answer = bin(int(bin1, 2) + int(bin2, 2))[2:]
    return answer