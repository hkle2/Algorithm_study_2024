class Solution:
    def maxWidthOfVerticalArea(self, points: List[List[int]]) -> int:
        answer = 0
        x_points = [x for x, y in points]
        x_points.sort()
        for i in range(1, len(x_points)):
            answer = max((x_points[i] - x_points[i-1]), answer)
        return answer