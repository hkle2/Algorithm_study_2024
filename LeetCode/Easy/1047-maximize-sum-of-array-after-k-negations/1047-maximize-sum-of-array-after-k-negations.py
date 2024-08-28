class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for n in range(k):
            i = nums.index(min(nums))
            nums[i] = -nums[i]
        return sum(nums)