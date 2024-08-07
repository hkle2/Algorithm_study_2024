class Solution:
    def generateTheString(self, n: int) -> str:
        # n이 홀수일 때와 짝수일 때를 구분지어 볼 것
        if n % 2 == 1:
            return "a" * n
        else:
            return "a" * (n-1) + "b"

# class Solution:
#     def generateTheString(self, n: int) -> str:
#         for i in range(n):
#             if n % 2 == 0:
#                 return "a" * (n-1) + "b"
#             else:
#                 return "a" * n