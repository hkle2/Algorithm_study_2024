class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        loc = word.find(ch)
        return word[:loc+1][::-1] + word[loc+1:]

class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        n = word.find(ch)
        if n != -1:
            return word[n::-1] + word[n+1:]
        else:
            return word