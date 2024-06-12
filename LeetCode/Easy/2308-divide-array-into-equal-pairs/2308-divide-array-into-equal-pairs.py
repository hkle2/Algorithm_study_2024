from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        answer = True
        nums_dict = Counter(nums)
        for i in nums_dict.values():
            if i % 2 != 0:
                answer = False
        return answer