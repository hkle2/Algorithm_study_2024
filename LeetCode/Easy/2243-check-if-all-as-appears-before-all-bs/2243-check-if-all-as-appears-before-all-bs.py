class Solution:
    def checkString(self, s: str) -> bool:
        appear_b = False
        for c in s:
            if c == "a":
                # a가 등장했는데 appear_b가 True라면 정답은 False!
                if appear_b:
                    return False
            elif c == "b":
                appear_b = True
        return True

# class Solution:
#     def checkString(self, s: str) -> bool:
#         for i in range(1, len(s)):
#             if s[i-1] == "b" and s[i] == "a":
#                 return False
#         return True