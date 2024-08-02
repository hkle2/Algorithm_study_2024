# class Solution:
#     def minMaxDifference(self, num: int) -> int:
#         # 가장 큰 수는 무조건 9로 치환한 수
#         # 가장 작은 수는 무조건 0으로 치환한 수
#         nums_str = str(num)
#         candidates = []
#         for i in range(10):
#             candidates.append(nums_str.replace(str(i), "9"))
#             candidates.append(nums_str.replace(str(i), "0"))
#         return max(candidates) - min(candidates)

class Solution:
    def minMaxDifference(self, num: int) -> int:
        num_str = str(num)
        max_num = num_str
        min_num = num_str
        for char in num_str:
            if char != "9":
                max_num = num_str.replace(char, "9")
                break
        for char in num_str:
            if char != "0":
                min_num = num_str.replace(char, "0")
                break
        return int(max_num) - int(min_num)

# class Solution:
#     def minMaxDifference(self, num: int) -> int:
#         nums = str(num)
#         m = int(nums.replace(nums[0], "0"))
#         for n in nums:
#             if n != "9":
#                 return int(nums.replace(n, "9")) - m
#         return num - m