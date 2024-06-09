def solution(strArr):
    answer = 0
    dict = {}
    for i in strArr:
        n = len(i)
        if n not in dict:
            dict[n] = 0
        dict[n] += 1
    answer = max(dict.values())
    return answer