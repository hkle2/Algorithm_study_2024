class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        answer = -1
        for i, num in enumerate(nums):
            if i % 10 == nums[i]:
                return i
        return answer

class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                return i
        return -1