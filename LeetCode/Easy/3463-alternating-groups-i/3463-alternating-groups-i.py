# class Solution:
#     def numberOfAlternatingGroups(self, colors: List[int]) -> int:
#         answer = 0
#         # for문, modulo 사용해줄 것
#         for i in range(len(colors)):
#             color_one = colors[i]
#             color_two = colors[(i+1) % len(colors)]
#             color_three = colors[(i+2) % len(colors)]
#             # color_one과 color_two가 서로 다르고
#             # color_two와 color_three가 서로 다른 경우
#             # alternating group 조건 성립! answer에 1 더해주기
#         return answer

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