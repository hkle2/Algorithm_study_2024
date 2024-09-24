class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        answer = 100000
        nums = [num for num in nums if num % 2 == 0]
        if not nums:
            return -1
        c = Counter(nums)
        for key, value in c.items():
            if value == max(c.values()):
                answer = min(key, answer)
        return answer

# class Solution:
#     def mostFrequentEven(self, nums: List[int]) -> int:
#         nums = [num for num in nums if num % 2 == 0]
#         c = Counter(nums)
#         c = sorted(c.items(), key=lambda x: (-x[1], x[0]))
#         if len(c) >= 1:
#             return c[0][0]
#         else:
#             return -1
# class Solution:
#     def mostFrequentEven(self, nums: List[int]) -> int:
#         answer = []
#         c = Counter(nums)
#         c = dict(filter(lambda x: x[0] % 2 == 0, c.items()))
#         c = sorted(c.items(), key=lambda x: (-x[1], x[0]))
#         if len(c) >= 1:
#             return c[0][0]
#         else:
#             return -1