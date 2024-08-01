class Solution:
    def minimumMoves(self, s: str) -> int:
        answer = 0
        i = 0
        while i < len(s):
            if s[i] == "X":
                answer += 1
                i += 3
            else:
                i += 1
        return answer

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