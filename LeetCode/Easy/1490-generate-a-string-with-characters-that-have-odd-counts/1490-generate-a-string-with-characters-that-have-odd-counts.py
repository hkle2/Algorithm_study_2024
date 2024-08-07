class Solution:
    def generateTheString(self, n: int) -> str:
        for i in range(n):
            if n % 2 == 0:
                answer = "a" * (n-1) + "b"
            else:
                answer = "a" * n
        return answer