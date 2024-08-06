# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         # while문 사용
#         # n이 1이 될 때까지 3으로 나눠보고
#         # 만약 3으로 나눠떨어지지 않는다면 3의 제곱수가 아닌 것
#         # n이 0보다 같거나 작은 경우 예외처리
#         if n <= 0:
#             return False
#         while True:
#             if n == 1:
#                 break
#             # 3으로 나눠떨어지면 3으로 나눠주고
#             # 만약 그렇지 않으면 False를 리턴
#             if n % 3 == 0:
#                 n /= 3
#             else:
#                 return False
#         return True

class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        # while문 사용
        # n이 1이 될 때까지 3으로 나눠보고
        # 만약 3으로 나눠떨어지지 않는다면 3의 제곱수가 아닌 것
        # n이 0보다 같거나 작은 경우 예외처리
        if n <= 0:
            return False
        while True:
            # 3으로 나눠떨어지면 3으로 나눠주고
            # 만약 그렇지 않으면 False를 리턴
            if n == 1:
                break
            if n % 3 == 0:
                n /= 3
            else:
                return False
        return True

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         while n > 0:
#             if n == 1:
#                 return True
#             elif n % 3 != 0:
#                 return False
#             n /= 3