class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        candidates = [x for x in arr if c[x] == 1]
        if k <= len(candidates):
            return candidates[k-1]
        return ""

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        answer = [key for key, value in c.items() if value == 1]
        if len(answer) >= k:
            return answer[k-1]
        return ""

class Solution:
    def kthDistinct(self, arr: List[str], k: int) -> str:
        c = Counter(arr)
        answer = []
        for key, value in c.items():
            if value == 1:
                answer.append(key)
        if len(answer) >= k:
            return answer[k-1]
        return ""