# class Solution:
#     def getNoZeroIntegers(self, n: int) -> List[int]:
#         # for
#         # 숫자를 문자열로 바꿔주기 / %를 사용해도 됨!
#         answer = []
#         for i in range(1, n):
#             a = i
#             b = n - a
#             # a와 b에 0이 포함되어 있지 않으면 
#             # [a, b]를 answer로 지정하고 break
#             print(a, b)
#         return answer
        
# class Solution:
#     def getNoZeroIntegers(self, n: int) -> List[int]:
#         for i in range(1, n):
#             a = i
#             b = n - a
#         return answer

class Solution:
    def getNoZeroIntegers(self, n: int) -> List[int]:
        for i in range(1, n):
            if "0" not in str(i) and "0" not in str(n-i):
                answer = [i, n-i]
                break
        return answer