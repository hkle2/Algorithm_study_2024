class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        answer = nums[0]
        sum_ = nums[0]
        for i in range(1, len(nums)):
            if nums[i-1] < nums[i]:
                sum_ += nums[i]
            else:
                sum_ = nums[i]
            answer = max(answer, sum_)
        return answer