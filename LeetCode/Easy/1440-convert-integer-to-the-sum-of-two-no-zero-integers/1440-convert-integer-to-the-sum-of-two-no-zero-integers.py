class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if "0" not in str(i) and "0" not in str(n - i):
                answer = [i, n-i]
                break
        return answer