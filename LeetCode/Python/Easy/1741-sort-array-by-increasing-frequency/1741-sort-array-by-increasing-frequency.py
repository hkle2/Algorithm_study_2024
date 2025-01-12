from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        return sorted(nums, key=lambda x: (c[x], -x))

from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        answer = []
        count_num = Counter(nums)
        answer = sorted(nums, key=lambda x: (count_num[x], -x))
        return answer