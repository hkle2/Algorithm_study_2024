def solution(s):
    answer = False
    p_cnt = 0
    y_cnt = 0
    for i in s:
        if i.lower() == "p":
            p_cnt += 1
        elif i.lower() == "y":
            y_cnt += 1
    if p_cnt == y_cnt:
        answer = True
    return answer

from collections import Counter

def solution(s):
    answer = True
    str = s.lower()
    s_counter = Counter(str)
    print(s_counter)
    if s_counter["p"] != s_counter["y"]:
        answer = False
    return answer

def solution(s):
    return s.lower().count("p") == s.lower().count("y")