class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    prices[i] -= prices[j]
                    break
        return prices

# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         answer = []
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 if prices[i] >= prices[j]:
#                     answer.append(prices[i] - prices[j])
#                     break
#                 if j == len(prices)-1:
#                     answer.append(prices[i])
#         answer.append(prices[-1])
#         return answer
