# class Solution:
#     def minOperations(self, nums: List[int], k: int) -> int:
#         # sorted
#         answer = 0
#         nums = sorted(nums)
#         for i in range(len(nums)):
#             if nums[i] >= k:
#                 answer = i
#                 break
#         return answer
#         # return len([num for num in nums if num < k])

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(len(nums)):
            if nums[i] < k:
                answer += 1
        return answer