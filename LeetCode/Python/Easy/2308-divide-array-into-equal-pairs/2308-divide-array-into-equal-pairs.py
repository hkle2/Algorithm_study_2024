from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_counter = Counter(nums)
        answer = True
        for key, value in nums_counter.items():
            if value % 2 != 0:
                answer = False
                break
        return answer

from collections import Counter

class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        answer = True
        nums_dict = Counter(nums)
        for i in nums_dict.values():
            if i % 2 != 0:
                answer = False
        return answer