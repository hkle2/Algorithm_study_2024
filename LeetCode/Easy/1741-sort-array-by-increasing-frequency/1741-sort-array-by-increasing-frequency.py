from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        answer = []
        num_dict = Counter(nums)
        answer = sorted(nums, key=lambda x: (num_dict[x], -x))
        return answer
