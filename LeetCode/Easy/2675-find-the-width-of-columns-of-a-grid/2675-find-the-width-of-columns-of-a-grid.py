class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        answer = []
        m = len(grid[0])
        n = len(grid)
        for i in range(m):
            length = 0
            for j in range(n):
                length = max(len(str(grid[j][i])), length)
            answer.append(length)
        return answer