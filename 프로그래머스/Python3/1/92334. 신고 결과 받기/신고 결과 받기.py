def solution(id_list, report, k):
    answer = []
    d_user = {}
    d_spam = {}
    spam = []
    for i in id_list:
        d_user[i] = []
        d_spam[i] = 0
    for r in report:
        u, s = r.split()
        if s not in d_user[u]:
            d_user[u] += [s]
            d_spam[s] += 1
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