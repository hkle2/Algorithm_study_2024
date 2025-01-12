class Solution:
    def countPoints(self, rings: str) -> int:
        d = defaultdict(set)
        for i in range(0, len(rings), 2):
            ring = rings[i]
            rod = rings[i+1]
        answer = 0
        for rod, colors in d.items():
            if len(colors) == 3:
                answer += 1
        return answer

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