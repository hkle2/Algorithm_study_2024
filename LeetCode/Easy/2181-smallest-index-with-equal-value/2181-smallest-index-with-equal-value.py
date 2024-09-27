class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        answer = 101
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                answer = min(i, answer)
        if answer == 101:
            return -1
        return answer