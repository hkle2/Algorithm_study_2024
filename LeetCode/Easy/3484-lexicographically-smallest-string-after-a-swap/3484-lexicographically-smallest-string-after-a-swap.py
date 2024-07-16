class Solution:
    def getSmallestString(self, s: str) -> str:
        l = []
        l.append(s)
        for i in range(len(s)-1):
            if int(s[i]) % 2 == int(s[i+1]) % 2:
                l.append(str(s[:i] + s[i+1] + s[i] + s[i+2:]))
        l.sort()
        if len(l) == 0:
            return s
        return l[0]

# class Solution:
#     def getSmallestString(self, s: str) -> str:
#         l = list(s)
#         answer = []
#         for i in range(len(l)-1):
#             a, b = int(l[i]), int(l[i+1])
#             if (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0):
#                 l[i], l[i+1] = l[i+1], l[i]
#                 answer.append("".join(l))
#         answer.sort(reverse=True)
#         if len(answer) == 0:
#             return s
#         else:
#             return answer[0]