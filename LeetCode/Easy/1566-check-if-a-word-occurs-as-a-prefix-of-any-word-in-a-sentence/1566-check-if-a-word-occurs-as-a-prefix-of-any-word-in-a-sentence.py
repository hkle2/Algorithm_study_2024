# class Solution:
#     def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
#         # split, enumerate, startswith
#         for i, s in enumerate(sentence.split(" ")):
#             if s.startswith(searchWord):
#                 return i + 1
#         return -1

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word = sentence.split(" ")
        for i in range(len(word)):
            if word[i].startswith(searchWord):
                return i + 1
        return -1