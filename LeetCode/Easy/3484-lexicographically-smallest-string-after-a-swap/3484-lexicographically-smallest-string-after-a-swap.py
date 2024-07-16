# class Solution:
#     def getSmallestString(self, s: str) -> str:
#         answer = [s]
#         for i in range(len(s) - 1):
#             if int(s[i]) % 2 == int(s[i+1]) % 2:
#                 swaped = s[:i] + s[i+1] + s[i] + s[i+2:]
#                 answer.append(swaped)
#         return sorted(answer)[0]

class Solution:
    def getSmallestString(self, s: str) -> str:
        l = [s]
        for i in range(len(s)-1):
            if int(s[i]) % 2 == int(s[i+1]) % 2:
                l.append(str(s[:i] + s[i+1] + s[i] + s[i+2:]))
        l.sort()
        return l[0]

# class Solution:
#     def getSmallestString(self, s: str) -> str:
#         for i in range(len(s)-1):
#             a, b = int(s[i]), int(s[i+1])
#             if a % 2 == b % 2 and a < b:
#                 return s[:i] + s[i+1] + s[i] + s[i+2:]
#         return s