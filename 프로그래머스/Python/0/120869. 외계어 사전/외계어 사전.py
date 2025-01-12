def solution(spell, dic):
    answer = 2
    for i in dic:
        result = 0
        for j in spell:
            if j in i:
                result += 1
        if result == len(spell):
            return 1
    return answer