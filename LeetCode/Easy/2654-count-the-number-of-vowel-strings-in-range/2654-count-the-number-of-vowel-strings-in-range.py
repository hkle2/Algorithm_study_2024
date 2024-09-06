# class Solution:
#     def vowelStrings(self, words: List[str], left: int, right: int) -> int:
#         vowels = ["a", 'e', 'i', 'o', 'u']
#         answer = 0
#         for i in range(left, right + 1):
#             word = words[i]
#             if word[0] in vowels and word[-1] in vowels:
#                 answer += 1
#         return answer

class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        answer = 0
        vowels = "aeiou"
        for i in range(left, right+1):
            if words[i][0] in vowels and words[i][-1] in vowels:
                answer += 1
        return answer