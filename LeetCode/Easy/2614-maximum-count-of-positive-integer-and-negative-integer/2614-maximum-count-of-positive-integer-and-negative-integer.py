class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        # for문 돌면서 양수 개수, 음수 개수 세주기
        pos = 0
        neg = 0
        for num in nums:
            # 양수면 pos에 1 더해주기
            # 음수면 neg에 1 더해주기
            if num > 0:
                pos += 1
            if num < 0:
                neg += 1
        return max(pos, neg)

# class Solution:
#     def maximumCount(self, nums: List[int]) -> int:
#         pos = 0
#         neg = 0
#         for i in range(len(nums)):
#             if nums[i] > 0:
#                 pos += 1
#             elif nums[i] < 0:
#                 neg += 1
#         if pos >= neg:
#             return pos
#         else:
#             return neg