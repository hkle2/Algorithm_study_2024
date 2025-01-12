def solution(id_list, report, k):
    answer = []
    d_user = {}
    d_spam = {}
    spam = []
    for i in id_list:
        d_user[i] = []
        d_spam[i] = 0
    for r in report:
        id1, id2 = r.split()
        if id2 not in d_user[id1]:
            d_user[id1] += [id2]
            d_spam[id2] += 1
    for key, value in d_spam.items():
        if value >= k:
            spam.append(key)
    for key, value in d_user.items():
        a = 0
        for i in range(len(value)):
            if value[i] in spam:
                a += 1
        answer.append(a)
    return answer

def solution(id_list, report, k):
    answer = []
    spam = {}
    mail = {}
    for r in report:
        id1, id2 = r.split()
        tmp = spam.get(id2, set())
        tmp.add(id1)
        spam[id2] = tmp
    for v in spam.values():
        if len(v) >= k:
            for id in v:
                mail[id] = mail.get(id, 0) + 1
    for id in id_list:
        answer.append(mail.get(id, 0))
    return answer