class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        quater = len(arr) / 4
        c = Counter(arr)
        for num, cnt in c.items():
            if cnt > quater:
                answer = num
        return answer

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for n in arr:
            if arr.count(n) > len(arr) * 0.25:
                return n
        return 0

from collections import Counter

class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        c = Counter(arr)
        for key, value in c.items():
            if value > len(arr) * 0.25:
                return key