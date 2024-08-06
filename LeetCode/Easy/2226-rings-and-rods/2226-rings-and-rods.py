class Solution:
    def countPoints(self, rings: str) -> int:
        answer = 0
        d = defaultdict()
        for i in range(0, len(rings), 2):
            if rings[i+1] not in d:
                d[rings[i+1]] = [rings[i]]
            else:
                d[rings[i+1]] += [rings[i]]
        for key, value in d.items():
            if len(set(value)) == 3:
                answer += 1
        return answer