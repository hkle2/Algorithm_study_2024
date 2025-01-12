class Solution:
    def isArraySpecial(self, nums: List[int]) -> bool:
        answer = True
        for i in range(len(nums)-1):
            if nums[i] % 2 == nums[i+1] % 2:
                answer = False
        return answer