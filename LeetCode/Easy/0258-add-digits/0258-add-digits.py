class Solution:
    def addDigits(self, num: int) -> int:
        while num >= 10:
            digit_sum = 0
            for c in str(num):
                digit_sum += int(c)
            num = digit_sum
        return num

class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while True:
            sum_ = 0
            for i in range(len(s)):
                sum_ += int(s[i])
            s = str(sum_)
            if len(s) == 1:
                break
        return int(s)