class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        answer = ""
        for word in words:
            # 만약 word가 palindrome이라면 answer에 word를 지정하고 break!
            # word[::-1]
            if word == word[::-1]:
                answer = word
                break
        return answer

class Solution:
    def firstPalindrome(self, words: List[str]) -> str:
        for i in words:
            if i == i[::-1]:
                return i
        return ""