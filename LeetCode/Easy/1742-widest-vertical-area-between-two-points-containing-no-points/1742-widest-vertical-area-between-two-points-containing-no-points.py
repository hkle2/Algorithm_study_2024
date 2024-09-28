class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        answer = 0
        x_points = [x for x, y in points]
        x_points.sort()
        for i in range(len(x_points)-1):
            answer = max((x_points[i+1] - x_points[i]), answer)
        return answer