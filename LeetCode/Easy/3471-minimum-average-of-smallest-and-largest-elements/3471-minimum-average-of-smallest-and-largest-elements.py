class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums = sorted(nums)
        averages = []
        while nums:
            min_num = nums.pop(0)
            max_num = nums.pop()
            averages.append((min_num + max_num) / 2)
        return min(averages)

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        averages = []
        n = len(nums) // 2
        for i in range(1, n+1):
            a, b = min(nums), max(nums)
            averages.append((a + b) / 2)
            nums.remove(a)
            nums.remove(b)
        return min(averages)