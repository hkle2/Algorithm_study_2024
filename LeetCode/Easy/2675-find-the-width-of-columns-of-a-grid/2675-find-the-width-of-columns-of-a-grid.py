class Solution:
    def findColumnWidth(self, grid: List[List[int]]) -> List[int]:
        answer = []
        for i in range(len(grid[0])):
            length = 0
            for j in range(len(grid)):
                if len(str(grid[j][i])) > length:
                    length = len(str(grid[j][i]))
            answer.append(length)
        return answer