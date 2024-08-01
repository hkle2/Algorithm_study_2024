class Solution:
    def minimumMoves(self, s: str) -> int:
        answer = 0
        c_list = [c for c in s]
        for i, c in enumerate(c_list):
            if c == "X":
                # 현재 위치의 문자 변경
                c_list[i] = "O"
                # 다음 위치의 문자 변경
                # 다다음 위치의 문자 변경
                # 이 때, 다음 혹은 다다음 위치가 범위를 벗어날 경우 예외처리
                answer += 1
                if i + 1 >= len(c_list):
                    continue
                c_list[i+1] = "O"
                if i + 2 >= len(c_list):
                    continue
                c_list[i+2] = "O"
        return answer

# class Solution:
#     def minimumMoves(self, s: str) -> int:
#         answer = 0
#         i = 0
#         while i < len(s):
#             if s[i] == "X":
#                 answer += 1
#                 i += 3
#             else:
#                 i += 1
#         return answer

# class Solution:
#     def minimumMoves(self, s: str) -> int:
#         s = list(s)
#         answer = 0
#         for i in range(len(s)-2):
#             if s[i] == "O" and i+3 < len(s):
#                 continue
#             cnt = 0
#             for j in range(3):
#                 if s[i+j] == "X":
#                     s[i+j] = "O"
#                     cnt += 1
#             if cnt != 0:
#                 answer += 1
#             if "X" not in s:
#                 return answer