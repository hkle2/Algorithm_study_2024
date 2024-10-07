class Solution:
    def romanToInt(self, s: str) -> int:
        d = {'I': 1, 'IV': 4, 'V': 5, 'IX': 9, 'X': 10, 'XL': 40, 'L': 50,
        'XC': 90, 'C': 100, 'CD': 400, 'D': 500, 'CM': 900, 'M': 1000}
        keys = sorted(d.keys(), key=lambda x: d[x], reverse=True)
        answer = 0
        while s:
            for key in keys:
                if s.startswith(key):
                    # answer에 해당 숫자만큼 더해주고
                    # s에서 해당 문자열을 잘라내 주기
                    answer += d[key]
                    s = s[len(key):]
                    break
        return answer

# class Solution:
#     def romanToInt(self, s: str) -> int:
#         roman_num = {"I": 1, "V": 5, "X": 10, "L": 50, "C": 100, "D": 500, "M": 1000}
#         answer = roman_num[s[0]]
#         for i in range(1, len(s)):
#             if roman_num[s[i]] - roman_num[s[i-1]] > 0:
#                 answer += (roman_num[s[i]] - 2 * roman_num[s[i-1]])
#             else:
#                 answer += roman_num[s[i]]
#         return answer