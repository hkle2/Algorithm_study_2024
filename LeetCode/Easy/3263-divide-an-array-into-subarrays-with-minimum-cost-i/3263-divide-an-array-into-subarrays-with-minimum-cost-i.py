class Solution:
    def minimumCost(self, nums: List[int]) -> int:
        answer = float("inf")
        for i in range(1, len(nums)-1):
            for j in range(i+1, len(nums)):
                # nums[:i] + nums[i+j] + nums[j:]
                answer = min(answer, (nums[0] + nums[i] + nums[j]))
        return answer
        