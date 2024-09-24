class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        even_num = [x for x in nums if x % 2 == 0]
        if not even_num:
            return -1
        c = Counter(even_num)
        max_freq = max(list(c.values()))
        candidates = [num for num, cnt in c.items() if cnt == max_freq]
        return sorted(candidates)[0]

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums = [num for num in nums if num % 2 == 0]
        if not nums:
            return -1
        c = Counter(nums)
        c = sorted(c.items(), key=lambda x: (-x[1], x[0]))
        return c[0][0]

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        answer = []
        c = Counter(nums)
        c = dict(filter(lambda x: x[0] % 2 == 0, c.items()))
        c = sorted(c.items(), key=lambda x: (-x[1], x[0]))
        if len(c) >= 1:
            return c[0][0]
        else:
            return -1