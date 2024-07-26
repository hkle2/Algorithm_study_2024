class Solution:
    def alternateDigitSum(self, n: int) -> int:
        answer = 0
        l = list(str(n))
        for i in range(0, len(l), 2):
            answer += int(l[i])
        for j in range(1, len(l), 2):
            answer -= int(l[j])
        return answer

# class Solution:
#     def alternateDigitSum(self, n: int) -> int:
#         answer = 0
#         l = list(str(n))
#         p = l.index(max(l))
#         print(p)
#         if p % 2 == 0:
#             for i in range(0, len(l), 2):
#                 answer += int(l[i])
#             for j in range(1, len(l), 2):
#                 answer -= int(l[j])
#         else:
#             for i in range(0, len(l), 2):
#                 answer -= int(l[i])
#             for j in range(1, len(l), 2):
#                 answer += int(l[j])
#         return answer