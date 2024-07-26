class Solution:
    def alternateDigitSum(self, n: int) -> int:
        answer = 0
        l = list(str(n))
        for i in range(len(l)):
            if i % 2 == 0:
                answer += int(l[i])
            else:
                answer -= int(l[i])
        return answer