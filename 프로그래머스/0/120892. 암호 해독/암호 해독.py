def solution(cipher, code):
    answer = ''
    print(len(cipher))
    for i in range(len(cipher)):
        if (i + 1) % code == 0:
            answer += cipher[i]
    return answer