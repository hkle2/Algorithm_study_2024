class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        answer = len(words)
        # words = set(words)
        for word in words:
            for i in range(len(word)):
                if word[i] not in allowed:
                    answer -= 1
                    break
        return answer

# class Solution:
#     def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
#         answer = 0
#         for word in words:
#             for i in range(len(word)):
#                 if word[i] not in allowed:
#                     answer += 1
#                     break
#         return len(words) - answer