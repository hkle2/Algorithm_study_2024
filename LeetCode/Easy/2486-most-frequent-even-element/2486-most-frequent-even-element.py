# class Solution:
#     def mostFrequentEven(self, nums: List[int]) -> int:
#         even_num = [x for x in nums if x % 2 == 0]
#         if not even_num:
#             return -1
#         c = Counter(even_num)
#         max_freq = max(list(c.values()))
#         # max_freq만큼 등장한 숫자들 찾아서 가장 작은 값을 리턴
#         print(c, max_freq)
#         return 0

class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        nums = [num for num in nums if num % 2 == 0]
        if not nums:
            return -1
        c = Counter(nums)
        return sorted(c.items(), key=lambda x: (-x[1], x[0]))[0][0]

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