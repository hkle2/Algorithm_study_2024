class Solution:
    def arraySign(self, nums: List[int]) -> int:
        answer = 1
        for num in nums:
            # 부호 판별해서 answer에 곱해주기
            if num == 0:
                # answer에 0 곱해준 뒤, break
                return 0
            elif num < 0:
                # answer에 -1 곱해주기
                answer *= -1
        return answer

# import math

# class Solution:
#     def arraySign(self, nums: List[int]) -> int:
#         p = math.prod(nums)
#         if p > 0:
#             answer = 1
#         elif p < 0:
#             answer = -1
#         else:
#             answer = 0
#         return answer

# class Solution:
#     def arraySign(self, nums: List[int]) -> int:
#         answer = 1
#         for i in nums:
#             if i > 0:
#                 answer *= 1
#             elif i < 0:
#                 answer *= -1
#             else:
#                 answer *= 0
#         return answer