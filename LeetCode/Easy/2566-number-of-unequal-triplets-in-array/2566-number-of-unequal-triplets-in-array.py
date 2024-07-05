# class Solution:
#     def unequalTriplets(self, nums: List[int]) -> int:
#        # 3중 for문
#        answer = 0
#        for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 for k in range(j+1, len(nums)):
#                     # 세 숫자가 모두 다른 경우에만 answer에 1 더해주기
#                     if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
#                         answer += 1
#        return answer

# class Solution:
#     def unequalTriplets(self, nums: List[int]) -> int:
#         answer = 0
#         n = len(nums)
#         for i in range(n):
#             for j in range(1, n):
#                 for k in range(2, n):
#                     if i < j and j < k:
#                         if nums[i] != nums[j] and nums[i] != nums[k] and nums[j] != nums[k]:
#                             answer += 1
#         return answer

from itertools import combinations

class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        answer = 0
        for num in combinations(nums, 3):
            if len(set(num)) == 3:
                answer += 1
        return answer