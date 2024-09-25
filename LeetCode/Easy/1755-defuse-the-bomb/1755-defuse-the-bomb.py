class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = []
        for i, num in enumerate(code):
            cur_sum = 0
            if k > 0:
                # 현재 위치에서 k개만큼 이후의 숫자들의 합 계산해서 추가
                for j in range(k):
                    cur_sum += code[(i + j + 1) % len(code)]
            else:
                # 현재 위치에서 k개만큼 이전 숫자들 합 계산해서 추가
                for j in range(-k):
                    cur_sum += code[i - j -1]
            answer.append(cur_sum)
        return answer

# class Solution:
#     def decrypt(self, code: List[int], k: int) -> List[int]:
#         n = len(code)
#         code = code * 2
#         if k == 0:
#             return [0] * n
#         elif k > 0:
#             for i in range(n):
#                 code[i] = sum(code[i+1:i+1+k])
#             return code[:n]
#         else:
#             for i in range(n):
#                 code[i] = sum(code[i+n+k:i+n])
#             return code[:n]

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