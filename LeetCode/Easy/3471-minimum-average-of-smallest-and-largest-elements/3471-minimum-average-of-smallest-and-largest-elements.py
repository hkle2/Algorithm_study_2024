class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        n = int(len(nums) / 2)
        nums.sort()
        for i in range(1, n+1):
            averages.append((nums[0] + nums[-1]) / 2)
            nums.pop(0)
            nums.pop()
        return min(averages)