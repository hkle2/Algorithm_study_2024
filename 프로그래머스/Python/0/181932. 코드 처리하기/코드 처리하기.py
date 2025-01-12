def solution(code):
    ret = ""
    mode = "0"
    for idx in range(len(code)):
        if mode == "0":
            if code[idx] != "1" and idx % 2 == 0:
                ret += code[idx]
            elif code[idx] == "1":
                mode = "1"
        else:
            if code[idx] != "1" and idx % 2 != 0:
                ret += code[idx]
            elif code[idx] == "1":
                mode = "0"
    if ret == "":
        ret = "EMPTY"
    return ret

def solution(code):
    ret = ""
    mode = 0
    for idx in range(len(code)):
        if code[idx] == "1":
            mode ^= 1
        else:
            if idx % 2 == mode:
                ret += code[idx]
    if ret == "":
        ret = "EMPTY"
    return ret

def solution(code):
    answer = "".join(code.split("1"))[::2]
    if not answer:
        answer = "EMPTY"
    return answer