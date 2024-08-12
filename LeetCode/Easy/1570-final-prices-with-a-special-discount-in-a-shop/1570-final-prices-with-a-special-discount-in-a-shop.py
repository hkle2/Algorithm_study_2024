class Solution:
    def finalPrices(self, prices: List[int]) -> List[int]:
        # 2중 for문 사용
        answer = []
        for i in range(len(prices)):
            discount = 0
            for j in range(i+1, len(prices)):
                if prices[i] >= prices[j]:
                    # discount 된 금액을 계산해서 answer에 추가
                    discount = prices[j]
                    break
            # flag 값이 True가 아니면 answer에 현재 가격 그대로 추가
            answer.append(prices[i] - discount)
        return answer

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

# class Solution:
#     def finalPrices(self, prices: List[int]) -> List[int]:
#         for i in range(len(prices)):
#             for j in range(i+1, len(prices)):
#                 if prices[i] >= prices[j]:
#                     prices[i] -= prices[j]
#                     break
#         return prices