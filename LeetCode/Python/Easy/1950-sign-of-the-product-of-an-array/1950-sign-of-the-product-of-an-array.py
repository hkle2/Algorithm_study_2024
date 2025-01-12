class Solution:
    def arraySign(self, nums: List[int]) -> int:
        answer = 1
        for num in nums:
            if num == 0:
                answer *= 0
                break
            elif num < 0:
                answer *= -1
        return answer

import math

class Solution:
    def arraySign(self, nums: List[int]) -> int:
        p = math.prod(nums)
        if p > 0:
            answer = 1
        elif p < 0:
            answer = -1
        else:
            answer = 0
        return answer

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