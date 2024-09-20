# from collections import Counter

# class Solution:
#     def getSneakyNumbers(self, nums: List[int]) -> List[int]:
#         answer = []
#         c = Counter(nums)
#         for key, value in c.items():
#             if value == 2:
#                 answer.append(key)
#         return answer

class Solution:
    def getSneakyNumbers(self, nums: List[int]) -> List[int]:
        seen = []
        answer = []
        for num in nums:
            if num not in seen:
                seen.append(num)
            else:
                answer.append(num)
        return answer
