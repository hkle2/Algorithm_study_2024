def solution(id_pw, db):
    id, pw = id_pw[0], id_pw[1]
    for ids, pws in db:
        if id == ids and pw == pws:
            return "login"
        elif id == ids and pw != pws:
            return "wrong pw"
    return "fail"

def solution(id_pw, db):
    id, pw = id_pw[0], id_pw[1]
    if dict(db).get(id):
        return "login" if dict(db).get(id) == pw else "wrong pw"
    return "fail"