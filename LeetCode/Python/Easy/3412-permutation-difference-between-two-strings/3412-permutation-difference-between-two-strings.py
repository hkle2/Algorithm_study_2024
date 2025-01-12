class Solution:
    def findPermutationDifference(self, s: str, t: str) -> int:
        answer = 0
        for i in range(len(s)):
            answer += abs(i - t.index(s[i]))
        return answer