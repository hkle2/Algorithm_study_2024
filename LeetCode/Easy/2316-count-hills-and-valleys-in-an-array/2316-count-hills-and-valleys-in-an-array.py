class Solution:
    def countHillValley(self, nums: List[int]) -> int:
        answer = 0
        for i in range(1, len(nums)-1):
            if nums[i] == nums[i+1]:
                nums[i] = nums[i-1]
            if nums[i-1] < nums[i] and nums[i] > nums[i+1]:
                answer += 1
            if nums[i-1] > nums[i] and nums[i] < nums[i+1]:
                answer += 1
        return answer