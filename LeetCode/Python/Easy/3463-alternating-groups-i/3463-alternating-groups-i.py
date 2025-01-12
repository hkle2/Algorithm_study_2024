class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        answer = 0
        for i in range(len(colors)):
            color_one = colors[i]
            color_two = colors[(i+1) % len(colors)]
            color_three = colors[(i+2) % len(colors)]
            if color_one != color_two and color_two != color_three:
                answer += 1
        return answer

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        answer = 0
        n = len(colors)
        for i in range(n):
            if colors[i-1] != colors[i-2] and colors[i-1] != colors[i]:
                answer += 1
        return answer

class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        answer = 0
        n = len(colors)
        for i in range(n):
            a, b, c = colors[i], colors[(i+1) % n], colors[(i+2) % n]
            if a != b and b != c:
                answer += 1
        return answer