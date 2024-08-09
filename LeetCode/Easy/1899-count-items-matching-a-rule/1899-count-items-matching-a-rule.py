# class Solution:
#     def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
#         answer = 0
#         if ruleKey == "type":
#            n = 0
#         elif ruleKey == "color":
#             n = 1
#         else:
#             n = 2
#         for i in range(len(items)):
#             if items[i][n] == ruleValue:
#                 answer += 1
#         return answer

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        answer = 0
        for i in range(len(items)):
            if ruleKey == "type":
                if items[i][0] == ruleValue:
                    answer += 1
            elif ruleKey == "color":
                if items[i][1] == ruleValue:
                    answer += 1
            else:
                if items[i][2] == ruleValue:
                    answer += 1
        return answer