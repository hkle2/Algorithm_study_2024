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