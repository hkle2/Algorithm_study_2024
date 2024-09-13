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
        cnt = []
        for c in s:
            if c in cnt:
                return c
            else:
                cnt.append(c)