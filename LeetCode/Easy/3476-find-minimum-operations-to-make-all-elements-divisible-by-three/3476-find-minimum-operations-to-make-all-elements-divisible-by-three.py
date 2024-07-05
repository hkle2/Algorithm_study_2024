class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        answer = 0
        for i in range(len(nums)):
            if nums[i] % 3 != 0:
                answer += 1
        return answer