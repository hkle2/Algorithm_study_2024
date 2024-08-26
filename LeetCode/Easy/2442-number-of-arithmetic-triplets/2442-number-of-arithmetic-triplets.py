class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        answer = 0
        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                for k in range(j+1, len(nums)):
                    if (nums[j] - nums[i] == diff) and (nums[k] - nums[j] == diff):
                        answer += 1
        return answer

from itertools import combinations

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        answer = 0
        for a, b, c in combinations(nums, 3):
            if (b - a == diff) and (c - b == diff):
                answer += 1
        return answer