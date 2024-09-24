class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        answer = []
        for i in range(len(grid[0])):
            length = 0
            for j in range(len(grid)):
                length = max(len(str(grid[j][i])), length)
            answer.append(length)
        return answer