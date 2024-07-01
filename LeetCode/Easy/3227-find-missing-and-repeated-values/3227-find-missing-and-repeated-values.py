from collections import Counter

class Solution:
    def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
        # 2중 for문을 사용할 것
        c = Counter()
        for i in range(len(grid)):
            for j in range(len(grid[0])):
                c[grid[i][j]] += 1
        answer = [-1, -1]
        # 1부터 n^2까지 반복을 진행하면서
        # 2번 등장한 값과 0번 등장한 값을 찾아서 answer에 지정하고 리턴
        for i in range(1, len(grid)**2+1):
            if c[i] == 2:
                answer[0] = i
            if c[i] == 0:
                answer[1] = i
        return answer

# class Solution:
#     def findMissingAndRepeatedValues(self, grid: List[List[int]]) -> List[int]:
#         answer = []
#         l = []
#         for i in range(len(grid)):
#             for j in range(len(grid)):
#                 if grid[i][j] not in l:
#                     l.append(grid[i][j])
#                 else:
#                     answer.append(grid[i][j])
#         for i in range(1, len(grid)**2+1):
#             if l.count(i) == 0:
#                 answer.append(i)
#         return answer