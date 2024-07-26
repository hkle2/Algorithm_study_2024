class Solution:
    def alternateDigitSum(self, n: int) -> int:
        answer = 0
        for i, c in enumerate(str(n)):
            # i가 홀수일 때와 짝수일 떄 신경써서 answer에 더해주기
            if i % 2 == 0:
                answer += int(c)
            else:
                answer -= int(c)
        return answer

# class Solution:
#     def alternateDigitSum(self, n: int) -> int:
#         answer = 0
#         l = list(str(n))
#         for i in range(0, len(l), 2):
#             answer += int(l[i])
#         for j in range(1, len(l), 2):
#             answer -= int(l[j])
#         return answer