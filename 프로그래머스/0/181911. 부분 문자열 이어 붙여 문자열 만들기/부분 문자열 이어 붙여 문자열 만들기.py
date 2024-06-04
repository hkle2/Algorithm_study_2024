def solution(my_strings, parts):
    answer = ''
    for s, (start, end) in zip(my_strings, parts):
        answer += s[start:end+1]
    return answer