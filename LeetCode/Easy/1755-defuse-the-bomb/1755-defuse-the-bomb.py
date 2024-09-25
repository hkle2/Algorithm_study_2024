class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        n = len(code)
        code = code * 2
        if k == 0:
            return [0] * n
        elif k > 0:
            for i in range(n):
                code[i] = sum(code[i+1:i+1+k])
            return code[:n]
        else:
            for i in range(n):
                code[i] = sum(code[i+n+k:i+n])
            return code[:n]

# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         answer = []
#         n = len(code)
#         if k == 0:
#             return [0] * n
#         elif k > 0:
#             for i in range(n):
#                 new = 0
#                 for j in range(1, k+1):
#                     new += code[(i + j) % n]
#                 answer.append(new)
#         else:
#             for i in range(n):
#                 new = 0
#                 for j in range(1, -k+1):
#                     new += code[i - j]
#                 answer.append(new)
#         return answer
