class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        x = sum(nums)
        y = 0
        for num in nums:
            for n in str(num):
                y += int(n)
        return abs(x - y)
        