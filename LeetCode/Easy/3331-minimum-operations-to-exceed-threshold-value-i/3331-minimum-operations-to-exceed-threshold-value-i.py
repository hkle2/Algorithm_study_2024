class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        for i in range(len(nums)):
            if nums[i] < k:
                answer += 1
        return answer