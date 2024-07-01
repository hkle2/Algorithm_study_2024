from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        c = Counter()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                c[grid[i][j]] += 1
        answer = [-1, -1]
        n = len(grid)
        for i in range(1, n*n+1):
            if c[i] == 2:
                answer[0] = i
            if c[i] == 0:
                answer[1] = i
        return answer

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        answer = [0, 0]
        l = []
        for i in range(len(grid)):
            for j in range(len(grid)):
                l.append(grid[i][j])
        for n in range(1, len(grid)**2+1):
            if l.count(n) == 2:
                answer[0] = n
            if l.count(n) == 0:
                answer[1] = n
        return answer