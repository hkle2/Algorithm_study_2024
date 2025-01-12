class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        if x < 10:
            return x
        answer = -1
        digit_sum = sum([int(c) for c in str(x)])
        if x % digit_sum == 0:
            return digit_sum
        return answer

class Solution:
    def sumOfTheDigitsOfHarshadNumber(self, x: int) -> int:
        s = str(x)
        num = 0
        for i in range(len(s)):
            num += int(s[i])
        if x % num == 0:
            return num
        else:
            return -1