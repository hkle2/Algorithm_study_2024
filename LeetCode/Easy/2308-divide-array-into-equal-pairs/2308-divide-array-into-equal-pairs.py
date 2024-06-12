from collections import Counter
class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        answer = True
        n = len(nums) / 2
        nums_dict = Counter(nums)
        for i in nums_dict.values():
            if i % 2 != 0:
                answer = False
                break
        return answer

        