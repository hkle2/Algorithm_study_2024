class Solution:
    def countAsterisks(self, s: str) -> int:
        answer = 0
        l = s.split("|")
        for i in range(0, len(l)+1, 2):
            answer += l[i].count("*")
        return answer