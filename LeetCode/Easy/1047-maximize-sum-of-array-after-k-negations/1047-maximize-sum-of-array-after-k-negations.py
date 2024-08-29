# class Solution:
#     def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
#         # 음수, 양수 각각 집계
#         answer = 0
#         pos_nums = sorted([x for x in nums if x >= 0])
#         neg_nums = sorted([x for x in nums if x < 0])
#         # K값이 neg_nums 길이보다 같거나 작을 때
#         # [4,2,3] 1
#         if k <= len(neg_nums):
#             answer += sum(pos_nums)
#             answer -= sum(neg_nums[:k])
#             answer += sum(neg_nums[k:])
#         else:
#             answer -= sum(neg_nums)
#             answer += sum(pos_nums)
#             # print(answer, len(neg_nums))
#             if (k - len(neg_nums)) % 2 == 1:
#                 answer -= (pos_nums[0] * 2)
#         return answer

class Solution:
    def largestSumAfterKNegations(self, nums: List[int], k: int) -> int:
        for n in range(k):
            i = nums.index(min(nums))
            nums[i] = -nums[i]
        return sum(nums)