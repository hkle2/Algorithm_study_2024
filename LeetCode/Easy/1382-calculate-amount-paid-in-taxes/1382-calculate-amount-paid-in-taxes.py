class Solution:
    def calculateTax(self, brackets: List[List[int]], income: int) -> float:
        answer = 0
        prev = 0
        for u, p in brackets:
            if u <= income:
                answer += (u - prev) * p / 100
                prev += (u - prev)
            else:
                answer += (income - prev) * p / 100
                break
        return answer

# class Solution:
#     def calculateTax(self, brackets: List[List[int]], income: int) -> float:
#         answer = 0
#         for i in range(len(brackets)):
#             inc = income
#             if i == 0:
#                 answer += brackets[i][0] * brackets[i][1] / 100
#             else:
#                 if brackets[i][0] <= income:
#                     answer += (brackets[i][0] - brackets[i-1][0]) * brackets[i][1] / 100
#                 else:
#                     answer += (brackets[i][0] - brackets[i-1][0]) * brackets[i][1] / 100
#                     break
#         return answer