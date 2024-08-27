class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min_value = min(nums)
            min_index = nums.index(min_value)
            nums[min_index] *= multiplier
        return nums
        
class Solution:
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            min_index = nums.index(min(nums))
            nums[min_index] *= multiplier
        return nums