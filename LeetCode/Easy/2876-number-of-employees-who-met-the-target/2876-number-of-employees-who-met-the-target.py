# class Solution:
#     def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
#         answer = 0
#         for hour in hours:
#             if hour >= target:
#                 answer += 1
#         return answer

class Solution:
    def numberOfEmployeesWhoMetTarget(self, hours: List[int], target: int) -> int:
        return sum([1 for hour in hours if hour >= target])