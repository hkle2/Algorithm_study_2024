class Solution:
    def addDigits(self, num: int) -> int:
        s = str(num)
        while True:
            answer = 0
            for i in range(len(s)):
                answer += int(s[i])
            s = str(answer)
            if len(s) == 1:
                break
        return int(s)