class Solution:
    def minOperations(self, nums: List[int]) -> int:
        prev = 0
        answer = 0
        for num in nums:
            if num > prev:
                prev = num
                continue
            inc = prev - num + 1
            answer += inc
            prev = num + inc
        return answer

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        prev = 0
        for num in nums:
            if prev >= num:
                answer += prev - num + 1
                prev += 1
            else:
                prev = num
        return answer

class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        for i in range(1, len(nums)):
            if nums[i] <= nums[i-1]:
                answer += nums[i-1] - nums[i] + 1
                nums[i] = nums[i-1] + 1
        return answer