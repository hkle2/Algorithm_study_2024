class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        # 1. k값이 numsOnes 보다 같거나 작을 때
        # 2. k값이 numsOnes 보다 크고 numOnes + numZeros 보다 같거나 작을 때
        # 3. 그보다 클 때
        return min(k, numOnes) if k <= numOnes + numZeros else numOnes - (k - (numOnes + numZeros))

# class Solution:
#     def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
#         if k <= numOnes:
#             return k
#         elif k <= numOnes + numZeros:
#             return numOnes
#         else:
#             return numOnes - (k - (numOnes + numZeros))