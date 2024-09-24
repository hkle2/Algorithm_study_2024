class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        answer = [0] * len(grid[0])
        # 2중 for문, 숫자 -> 문자열로 변환
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                num_len = len(str(grid[i][j]))
                answer[j] = max(answer[j], num_len)
        return answer

# class Solution:
#     def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
#         answer = []
#         for i in range(len(grid[0])):
#             length = 0
#             for j in range(len(grid)):
#                 if len(str(grid[j][i])) > length:
#                     length = len(str(grid[j][i]))
#             answer.append(length)
#         return answer