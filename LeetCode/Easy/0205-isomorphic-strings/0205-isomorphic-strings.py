class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            print(s[i], t[i], d)
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            else:
                if t[i] in d.values():
                    return False
                d[s[i]] = t[i]
        return True

class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        answer = True
        d = {}
        for i in range(len(s)):
            if s[i] in d.keys():
                if d[s[i]] != t[i]:
                    answer = False
            elif t[i] in d.values():
                answer = False
            else:
                d[s[i]] = t[i]
        return answer