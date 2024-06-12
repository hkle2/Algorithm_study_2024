# class Solution:
#     def separateDigits(self, nums: List[int]) -> List[int]:
#         answer = []
#         for num in nums:
#             num_str = str(num)
#             for c in num_str:
#                 print(c, type(c))
#                 # 숫자를 문자로 바꿔서 한글자씩 읽어오는데 성공!
#                 # 이를 다시 숫자로 바꿔서 answer에 append
#                 answer.append(int(s[j]))
#         return answer

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            s = str(i)
            for j in s:
                answer.append(int(j))
        return answer