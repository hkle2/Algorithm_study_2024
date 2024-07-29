class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit = []
        double_digit = []
        # 1. 한자리 수만 모아서 single_digit에 추가하기
        # 2. 두자리 수만 모아서 double_digit에 추가하기
        # 전체 합계에서 single_digits 합계를 빼준 값과 비교
        # 전체 합계에서 double_digits 합계를 빼준 값과 비교
        for num in nums:
            if num < 10:
                single_digit.append(num)
            elif num < 100:
                double_digit.append(num)
        total_sum = sum(nums)
        single_sum = sum(single_digit)
        double_sum = sum(double_digit)
        print(total_sum, single_sum, double_sum)
        if single_sum != double_sum:
            return True
        return False
        
# class Solution:
#     def canAliceWin(self, nums: List[int]) -> bool:
#         single = 0
#         double = 0
#         for num in nums:
#             if num < 10:
#                 single += num
#             else:
#                 double += num
#         if single != double:
#             return True
#         return False