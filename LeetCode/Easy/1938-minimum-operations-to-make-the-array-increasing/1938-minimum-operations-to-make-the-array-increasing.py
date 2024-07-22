class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                answer += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        return answer

# class Solution:
#     def minOperations(self, nums: List[int]) -> int:
#         answer = 0
#         prev = 0
#         for num in nums:
#             if prev >= num:
#                 answer += prev - num + 1
#                 prev = prev + 1
#             else:
#                 prev = num
#         return answer