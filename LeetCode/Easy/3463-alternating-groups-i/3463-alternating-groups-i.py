class Solution:
    def numberOfAlternatingGroups(self, colors: List[int]) -> int:
        answer = 0
        n = len(colors)
        for i in range(n):
            a, b, c = colors[i], colors[(i+1) % n], colors[(i+2) % n]
            if a != b and b != c:
                answer += 1
        return answer

# class Solution:
#     def numberOfAlternatingGroups(self, colors: List[int]) -> int:
#         answer = 0
#         n = len(colors)
#         for i in range(n):
#             if i > 0 and i < n - 1:
#                 if (colors[i] != colors[i+1]) and (colors[i] != colors[i-1]):
#                     answer += 1
#             elif i == 0:
#                 if colors[i] != colors[i+1] and colors[i] != colors[-1]:
#                     answer += 1
#             else:
#                 if colors[i] != colors[0] and colors[i] != colors[i-1]:
#                     answer += 1
#         return answer