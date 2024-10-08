class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        c = Counter(nums)
        answer = 0
        for num in nums:
            if num + k in c:
                answer += c[num+k]
        return answer

# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         answer = 0
#         for a, b in combinations(nums, 2):
#             if abs(a - b) == k:
#                 answer += 1
#         return answer

# class Solution:
#     def countKDifference(self, nums: List[int], k: int) -> int:
#         answer = 0
#         for i in range(len(nums)):
#             for j in range(i+1, len(nums)):
#                 if abs(nums[i] - nums[j]) == k:
#                     answer += 1
#         return answer