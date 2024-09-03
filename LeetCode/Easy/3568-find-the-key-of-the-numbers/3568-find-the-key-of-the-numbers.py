class Solution:
    def generateKey(self, num1: int, num2: int, num3: int) -> int:
        # zip
        str_1 = str(num1).zfill(4)
        str_2 = str(num2).zfill(4)
        str_3 = str(num3).zfill(4)
        answer = ""
        for chr_1, chr_2, chr_3 in zip(str_1, str_2, str_3):
            answer += min(chr_1, chr_2, chr_3)
        return int(answer)
        
# class Solution:
#     def generateKey(self, num1: int, num2: int, num3: int) -> int:
#         str1 = str(num1).zfill(4)
#         str2 = str(num2).zfill(4)
#         str3 = str(num3).zfill(4)
#         answer = ""
#         for i in range(4):
#             answer += min(str1[i], str2[i], str3[i])
#         return int(answer)