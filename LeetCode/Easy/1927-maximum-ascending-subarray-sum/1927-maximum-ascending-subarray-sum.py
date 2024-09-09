class Solution:
    def maxAscendingSum(self, nums: List[int]) -> int:
        prev = 0
        cur_sum = 0
        answer = 0
        for num in nums:
            if num > prev:
                cur_sum += num
            else:
                cur_sum = num
            answer = max(answer, cur_sum)
            prev = num
        return answer

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