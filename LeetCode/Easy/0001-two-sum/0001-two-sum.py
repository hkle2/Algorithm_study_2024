class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        length = len(nums)
    
        
        for idx1, num1 in enumerate(nums):
            for idx2 in range(idx1+1, length):
                num2 = nums[idx2]
                _sum = num1 + num2 
                
                if _sum == target:
                    return [idx1, idx2] 
        