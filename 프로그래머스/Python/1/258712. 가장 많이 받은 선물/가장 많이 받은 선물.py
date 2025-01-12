def solution(friends, gifts):
    answer = []
    record = {}
    score = {}
    for gift in gifts:
        id1, id2 = gift.split()
        record[id1] = record.get(id1, {})
        record[id1][id2] = record[id1].get(id2, 0) + 1
    for f in friends:
        if f in record:
            score[f] = sum(record.get(f).values())
        else:
            score[f] = 0
    for s1 in score:
        for s2 in score:
            if s1 == s2:
                continue
            elif s2 in record:
                score[s1] -= record.get(s2).get(s1, 0)
    for f1 in friends:
        gift = 0
        for f2 in friends:
            if f1 == f2:
                continue
            tmp = record.get(f1, {}).get(f2, 0) - record.get(f2, {}).get(f1, 0)
            if tmp > 0:
                gift += 1
            elif tmp == 0 and score[f1] > score[f2]:
                gift += 1
        answer.append(gift)
    return max(answer)

def solution(friends, gifts):
    answer = []
    record = {}
    score = {}
    for gift in gifts:
        id1, id2 = gift.split()
        record[id1] = record.get(id1, {})
        record[id1][id2] = record[id1].get(id2, 0) + 1
        record[id2] = record.get(id2, {})
        record[id2][id1] = record[id2].get(id1, 0) - 1
    for f in friends:
        if f in record:
            score[f] = sum(record.get(f).values())
        else:
            score[f] = 0
    for f1 in friends:
        gift = 0
        for f2 in friends:
            if f1 == f2:
                continue
            tmp = record.get(f1, {}).get(f2, 0) - record.get(f2, {}).get(f1, 0)
            if tmp > 0:
                gift += 1
            elif tmp == 0 and score[f1] > score[f2]:
                gift += 1
        answer.append(gift)
    return max(answer)