class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        answer = 0
        points = sorted(points, key=lambda x: x[0])
        for i in range(len(points)-1):
            answer = max((points[i+1][0] - points[i][0]), answer)
        return answer