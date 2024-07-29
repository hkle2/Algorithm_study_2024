class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        d = {}
        for i in range(len(s)):
            if s[i] in d:
                if d[s[i]] != t[i]:
                    return False
            elif t[i] in d.values():
                return False
            else:
                d[s[i]] = t[i]
        return True

# class Solution:
#     def isIsomorphic(self, s: str, t: str) -> bool:
#         answer = True
#         for i in range(1, len(s)):
#             if (s[i-1] != t[i-1]) or (s[i] != t[i]):
#                 if (s[i-1] == s[i] and t[i-1] != t[i]) or (s[i-1] != s[i] and t[i-1] == t[i]):
#                     answer = False
#         return answer