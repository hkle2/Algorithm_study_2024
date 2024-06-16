def solution(id_pw, db):
    answer = ''
    id, pw = id_pw[0], id_pw[1]
    for ids, pws in db:
        if id == ids and pw == pws:
            answer = "login"
        elif id == ids and pw != pws:
            answer = "wrong pw"
        else:
            continue
    if not answer:
        answer = "fail"
    return answer