def solution(array):
    s = "".join(map(str, array))
    answer = s.count("7")
    return answer