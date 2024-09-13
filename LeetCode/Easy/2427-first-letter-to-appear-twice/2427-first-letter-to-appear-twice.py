# from collections import defaultdict

# class Solution:
#     def repeatedCharacter(self, s: str) -> str:
#         # for, dictionary
#         d = defaultdict(int)
#         for c in s:
#             d[c] += 1
#             # 특정 글자가 2번 이상 등장하면 return 해주기!
#             if d[c] == 2:
#                 return c

class Solution:
    def repeatedCharacter(self, s: str) -> str:
        visited = set()
        for c in s:
            if c in visited:
                return c
            else:
                visited.add(c)

# class Solution:
#     def repeatedCharacter(self, s: str) -> str:
#         visited = []
#         for i in range(len(s)):
#             if s[i] in visited:
#                 return s[i]
#             else:
#                 visited.append(s[i])