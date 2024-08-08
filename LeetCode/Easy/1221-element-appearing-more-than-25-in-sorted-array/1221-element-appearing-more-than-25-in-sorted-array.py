from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        for key, value in c.items():
            if value > len(arr) * 0.25:
                return key

# class Solution:
#     def findSpecialInteger(self, arr: List[int]) -> int:
#         for n in arr:
#             if arr.count(n) > len(arr) * 0.25:
#                 return n
#         return 0