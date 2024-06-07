def solution(age):
    s = str(age)
    answer = s.translate(s.maketrans("0123456789", "abcdefghij"))
    return answer