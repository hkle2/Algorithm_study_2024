# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         answer = []
#         for i in range(len(nums)):
#             for j in range(len(nums)):
#                 if i == j:
#                     continue
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         length = len(nums)
#         for i, num1 in enumerate(nums):
#             for j in range(i+1, length):
#                 if num1 + nums[j] == target:
#                     return [i, j]

# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if nums[i] + nums[j] == target:
#                     return [i, j]

class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        d = {}
        for i, num in enumerate(nums):
            diff = target - num
            if diff in d:
                return [d[diff], i]
            d[num] = i