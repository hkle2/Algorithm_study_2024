class Solution:
    def minMaxDifference(self, num: int) -> int:
        nums = str(num)
        m = int(nums.replace(nums[0], "0"))
        for n in nums:
            if n != "9":
                return int(nums.replace(n, "9")) - m
        return num - m

# class Solution:
#     def minMaxDifference(self, num: int) -> int:
#         max_answer = ""
#         min_answer = ""
#         num_list = list(str(num))
#         max_i = num_list[0]
#         for i in range(len(num_list)):
#             if num_list[i] == num_list[0]:
#                 if num_list[i] == "9":
#                     max_answer += str(num_list[i])
#                 else:
#                     max_answer += "9"
#             else:
#                 max_answer += str(num_list[i])
#         for i in range(len(num_list)):
#             if num_list[i] == num_list[0]:
#                 min_answer += "0"
#             else:
#                 min_answer += str(num_list[i])
#         return int(max_answer) - int(min_answer)