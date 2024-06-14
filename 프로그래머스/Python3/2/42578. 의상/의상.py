def solution(clothes):
    answer = 1
    clothes_dict = {}
    for value, key in clothes:
        if key not in clothes_dict:
            clothes_dict[key] = ["none"]
        clothes_dict[key] += [value]
    print(clothes_dict)
    for i in clothes_dict.values():
        answer *= len(i)
    answer -= 1
    return answer