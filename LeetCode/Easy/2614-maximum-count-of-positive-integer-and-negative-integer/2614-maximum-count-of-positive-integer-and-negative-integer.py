class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        answer = 0
        pos = 0
        neg = 0
        for i in range(len(nums)):
            if nums[i] > 0:
                pos += 1
            elif nums[i] < 0:
                neg += 1
        if pos >= neg:
            answer = pos
        else:
            answer = neg
        return answer