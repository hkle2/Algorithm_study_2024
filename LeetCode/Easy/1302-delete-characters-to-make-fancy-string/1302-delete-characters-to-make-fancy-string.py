# class Solution:
#     def makeFancyString(self, s: str) -> str:
#         answer = ""
#         prev = ""
#         cnt = 0
#         for c in s:
#             if c == prev:
#                 cnt += 1
#             else:
#                 cnt = 1
#             if cnt < 3:
#                 answer += c
#             prev = c
#         return answer

class Solution:
    def makeFancyString(self, s: str) -> str:
        seen = []
        for c in s:
            if (len(seen) >= 2) and (c == seen[-1]) and (c == seen[-2]):
                continue
            else:
                seen.append(c)
        return "".join(seen)