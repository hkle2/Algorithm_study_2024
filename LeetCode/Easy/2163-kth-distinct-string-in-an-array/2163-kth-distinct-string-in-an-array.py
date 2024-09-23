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