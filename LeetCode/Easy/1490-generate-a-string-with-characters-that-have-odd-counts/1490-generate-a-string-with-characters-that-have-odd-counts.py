class Solution:
    def generateTheString(self, n: int) -> str:
        answer = ""
        for i in range(n):
            if n % 2 != 0:
                answer = "a" * n
            else:
                answer = "a" * (n-1) + "b"
        return answer