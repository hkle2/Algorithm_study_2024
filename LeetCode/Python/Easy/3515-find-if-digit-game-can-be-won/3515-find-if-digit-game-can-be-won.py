class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single_digit = []
        double_digit = []
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
        
class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        single = 0
        double = 0
        for num in nums:
            if num < 10:
                single += num
            else:
                double += num
        if single != double:
            return True
        return False