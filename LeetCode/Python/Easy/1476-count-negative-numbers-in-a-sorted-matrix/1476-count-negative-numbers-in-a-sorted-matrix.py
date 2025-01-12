class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        return sum([1 for row in grid for num in row if num < 0])

class Solution:
    def countNegatives(self, grid: List[List[int]]) -> int:
        answer = 0
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] < 0:
                    answer += 1
        return answer