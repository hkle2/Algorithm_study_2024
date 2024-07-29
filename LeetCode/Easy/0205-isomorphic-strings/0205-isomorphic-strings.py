class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        answer = True
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    answer = False
            elif t[i] in d.values():
                answer = False
            else:
                d[s[i]] = t[i]
        return answer