class Solution:
    def arraySign(self, nums: List[int]) -> int:
        answer = 1
        for i in nums:
            if i > 0:
                answer *= 1
            elif i < 0:
                answer *= -1
            else:
                answer *= 0
        return answer
                