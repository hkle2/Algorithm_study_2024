class Solution:
    def romanToInt(self, s: str) -> int:
        roman_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
        answer = roman_num[s[0]]
        for i in range(1, len(s)):
            tmp = roman_num[s[i]] - roman_num[s[i-1]]
            print(tmp)
            if tmp > 0:
                answer -= roman_num[s[i-1]]
                answer += (roman_num[s[i]] - roman_num[s[i-1]])
            else:
                answer += roman_num[s[i]]
        return answer