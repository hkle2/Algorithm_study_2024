# class Solution:
#     def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
#         matrix = [[0 for x in range(n)] for y in range(m)]
#         for row in matrix:
#         answer = 0
#         for row, col in indices:
#             for i in range(n):
#                 matrix[row][i] += 1
#             for i in range(m):
#                 matrix[i][col] += 1
#         for i in range(m):
#             for j in range(n):
#                 if matrix[i][j] % 2 == 1:
#                     answer += 1
#         return answer

# class Solution:
#     def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
#         answer = 0
#         mat = np.zeros(m, n)
#         for r, c in indices:
#             mat[r] += 1
#             mat[:, c] += 1
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] % 2 != 0:
#                     answer += 1
#         return answer

# class Solution:
#     def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
#         answer = 0
#         mat = [[0 for _ in range(n)] for _ in range(m)]
#         for r, c in indices:
#             mat[r] = [x + 1 for x in mat[r]]
#             for col in mat:
#                 col[c] += 1
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
            for i in range(n):
                mat[r][i] += 1
            for i in range(m):
                mat[i][c] += 1
        for i in range(m):
            for j in range(n):
                if mat[i][j] % 2 != 0:
                    answer += 1
        return answer