# import numpy as np

# class Solution:
#     def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
#         answer = 0
#         mat = np.zeros((m, n))
#         for r, c in indices:
#             mat[r] += 1
#             mat[:, c] += 1
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] % 2 != 0:
#                     answer += 1
#         return answer

class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        answer = 0
        mat = [[0 for _ in range(n)] for _ in range(m)]
        for r, c in indices:
            mat[r] = [x + 1 for x in mat[r]]
            for col in mat:
                col[c] += 1
        for i in range(m):
            for j in range(n):
                if mat[i][j] % 2 != 0:
                    answer += 1
        return answer

# class Solution:
#     def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
#         answer = 0
#         mat = [[0 for _ in range(n)] for _ in range(m)]
#         for r, c in indices:
#             for i in range(n):
#                 mat[r][i] += 1
#             for i in range(m):
#                 mat[i][c] += 1
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] % 2 != 0:
#                     answer += 1
#         return answer