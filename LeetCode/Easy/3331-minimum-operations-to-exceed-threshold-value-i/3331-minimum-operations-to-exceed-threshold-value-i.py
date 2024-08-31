class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        # sorted
        answer = 0
        nums = sorted(nums)
        for i in range(len(nums)):
            if nums[i] >= k:
                return i

# class Solution:
#     def minOperations(self, nums: List[int], k: int) -> int:
#         return len([num for num in nums if num < k])

# class Solution:
#     def minOperations(self, nums: List[int], k: int) -> int:
#         answer = 0
#         for num in nums:
#             if num < k:
#                 answer += 1
#         return answer