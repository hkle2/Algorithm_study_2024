class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        answer = []
        l = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                if grid[i][j] not in l:
                    l.append(grid[i][j])
                else:
                    answer.append(grid[i][j])
        for i in range(1, len(grid)**2+1):
            if l.count(i) == 0:
                answer.append(i)
        return answer