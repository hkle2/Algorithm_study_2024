class Solution:
    def generateTheString(self, n: int) -> str:
        for i in range(n):
            if n % 2 == 0:
                return "a" * (n-1) + "b"
            else:
                return "a" * n