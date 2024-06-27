class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        answer = ""
        n = word.find(ch)
        if n != -1:
            answer = word[n::-1] + word[n+1:]
        else:
            answer = word
        return answer