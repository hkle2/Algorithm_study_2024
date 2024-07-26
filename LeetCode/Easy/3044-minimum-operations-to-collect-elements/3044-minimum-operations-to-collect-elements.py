class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        num = set()
        for i, n in enumerate(reversed(nums)):
            print(i, n)
            if n > k:
                continue
            num.add(n)
            if len(num) == k:
                return i + 1

# class Solution:
#     def minOperations(self, nums: List[int], k: int) -> int:
#         answer = 0
#         num = []
#         for i in range(1, k+1):
#             num.append(i)
#         nums.reverse()
#         for i in range(len(nums)):
#             if nums[i] in num:
#                 num.remove(nums[i])
#                 if num != []:
#                     answer += 1
#         answer += 1
#         return answer