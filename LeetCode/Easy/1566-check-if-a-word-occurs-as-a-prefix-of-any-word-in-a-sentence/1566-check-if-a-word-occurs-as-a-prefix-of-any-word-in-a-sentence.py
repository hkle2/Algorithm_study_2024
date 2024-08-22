class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        answer = -1
        word_list = sentence.split(" ")
        for i, word in enumerate(word_list):
            if word.startswith(searchWord):
                answer = i + 1
                break
        return answer

class Solution:
    def isPrefixOfWord(self, sentence: str, searchWord: str) -> int:
        word = sentence.split(" ")
        for i in range(len(word)):
            if word[i].startswith(searchWord):
                return i + 1
        return -1