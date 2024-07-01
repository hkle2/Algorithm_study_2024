from collections import Counter

class Solution:
    def frequencySort(self, nums: List[int]) -> List[int]:
        # sorted, counter
        c = Counter(nums)
        # 큰 숫자가 앞으로, 작은 숫자가 뒤로
        return sorted(nums, key=lambda x: (c[x], -x))

# from collections import Counter

# class Solution:
#     def frequencySort(self, nums: List[int]) -> List[int]:
#         answer = []
#         count_num = Counter(nums)
#         answer = sorted(nums, key=lambda x: (count_num[x], -x))
#         return answer