from collections import Counter

class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        answer = 0
        nums_dict = Counter(nums)
        for i, j in nums_dict.items():
            if j == max(nums_dict.values()):
                answer += j
        return answer