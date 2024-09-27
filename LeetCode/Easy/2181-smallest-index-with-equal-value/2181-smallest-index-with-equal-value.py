class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        answer = -1
        # for, enumerate
        for i, num in enumerate(nums):
            # i mod 10 == nums[i] 조건 맞으면 i를 answer 지정 후 break
            if i % 10 == nums[i]:
                return i
        return answer

# class Solution:
#     def smallestEqual(self, nums: List[int]) -> int:
#         for i in range(len(nums)):
#             if i % 10 == nums[i]:
#                 return i
#         return -1