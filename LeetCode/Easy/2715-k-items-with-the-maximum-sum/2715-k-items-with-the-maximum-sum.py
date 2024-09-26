class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        return min(k, numOnes) if k <= numOnes + numZeros else numOnes - (k - (numOnes + numZeros))

class Solution:
    def kItemsWithMaximumSum(self, numOnes: int, numZeros: int, numNegOnes: int, k: int) -> int:
        if k <= numOnes:
            return k
        elif k <= numOnes + numZeros:
            return numOnes
        else:
            return numOnes - (k - (numOnes + numZeros))