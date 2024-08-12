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