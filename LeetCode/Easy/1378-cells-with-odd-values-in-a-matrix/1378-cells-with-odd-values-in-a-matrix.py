class Solution:
    def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
        matrix = [[0 for x in range(n)] for y in range(m)]
        for row in matrix:
            print(row)
        answer = 0
        for row, col in indices:
            for i in range(n):
                # 특정 row의 값을 1씩 증가시켜 주기
                matrix[row][i] += 1
            for i in range(m):
                # 특정 column 값을 1씩 증가시켜 주기
                matrix[i][col] += 1
        # 전체 matrix 순회하면서 홀수 개수 세어서 리턴
        for i in range(m):
            for j in range(n):
                if matrix[i][j] % 2 == 1:
                    answer += 1
        return answer

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

# class Solution:
#     def oddCells(self, m: int, n: int, indices: List[List[int]]) -> int:
#         answer = 0
#         mat = [[0 for _ in range(n)] for _ in range(m)]
#         for i in range(len(indices)):
#             r, c = indices[i]
#             for j in range(n):
#                 mat[r][j] += 1
#             for k in range(m):
#                 mat[k][c] += 1
#         for i in range(m):
#             for j in range(n):
#                 if mat[i][j] % 2 != 0:
#                     answer += 1
#         return answer