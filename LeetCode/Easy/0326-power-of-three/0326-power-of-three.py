class Solution:
    def isPowerOfThree(self, n: int) -> bool:
        for i in range(31):
            squared_num = math.pow(3, i)
            if n == squared_num:
                return True
            elif n < squared_num:
                return False
        return False

# class Solution:
#     def isPowerOfThree(self, n: int) -> bool:
#         if n <= 0:
#             return False
#         while True:
#             if n == 1:
#                 break
#             if n % 3 == 0:
#                 n /= 3
#             else:
#                 return False
#         return True

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