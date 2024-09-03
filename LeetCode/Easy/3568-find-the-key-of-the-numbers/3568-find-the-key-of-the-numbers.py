class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        str1 = str(num1).zfill(4)
        str2 = str(num2).zfill(4)
        str3 = str(num3).zfill(4)
        answer = ""
        for i in range(4):
            answer += min(str1[i], str2[i], str3[i])
        return int(answer)