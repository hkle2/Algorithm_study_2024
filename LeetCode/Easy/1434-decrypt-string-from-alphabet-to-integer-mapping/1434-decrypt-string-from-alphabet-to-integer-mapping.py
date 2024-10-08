class Solution:
    def freqAlphabets(self, s: str) -> str:
        d = {}
        for i in range(1, 27):
            if i < 10:
                d[str(i)] = chr(i+96)
            else:
                d[str(i) + "#"] = chr(i+96)
        sorted_d = sorted(d.keys(), reverse=True, key=lambda x: len(x))
        answer = ""
        while s:
            for key in sorted_d:
                if s.startswith(key):
                    answer += d[key]
                    s = s[len(key):]
                    break
        return answer