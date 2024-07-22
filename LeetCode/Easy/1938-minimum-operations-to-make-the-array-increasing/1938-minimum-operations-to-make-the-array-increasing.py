class Solution:
    def minOperations(self, nums: List[int]) -> int:
        answer = 0
        prev = 0
        for num in nums:
            if prev >= num:
                answer += prev - num + 1
                prev = prev + 1
            else:
                prev = num
        return answer