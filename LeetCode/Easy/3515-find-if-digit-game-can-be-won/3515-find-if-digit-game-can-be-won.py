class Solution:
    def canAliceWin(self, nums: List[int]) -> bool:
        answer = False
        single = 0
        double = 0
        for num in nums:
            if num < 10:
                single += num
            else:
                double += num
        if single != double:
            answer = True
        return answer