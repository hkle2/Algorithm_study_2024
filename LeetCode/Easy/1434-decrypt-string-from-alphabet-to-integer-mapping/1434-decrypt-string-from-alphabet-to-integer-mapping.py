class Solution:
    def freqAlphabets(self, s: str) -> str:
        d = {}
        for i in range(26):
            alphabet = chr(i + 97)
            num = i + 1
            if num < 10:
                d[str(num)] = alphabet
            else:
                d[str(num) + "#"] = alphabet
        sorted_keys = sorted(d.keys(), reverse=True, key=lambda x: (len(x), x))
        answer = ""
        while s:
            for key in sorted_keys:
                if s.startswith(key):
                    answer += d[key]
                    s = s[len(key):]
                    break
        return answer

class Solution:
    def freqAlphabets(self, s: str) -> str:
        answer = ""
        i = 0
        while i < len(s):
            if i + 2 < len(s) and s[i+2] == "#":
                answer += chr(int(s[i:i+2]) + ord("a") - 1)
                i += 3
            else:
                answer += chr(int(s[i]) + ord("a") - 1)
                i += 1
        return answer