class Solution:
    def decrypt(self, code: List[int], k: int) -> List[int]:
        answer = []
        n = len(code)
        if k > 0:
            for i in range(n):
                new = 0
                for j in range(1, k+1):
                    new += code[(i + j) % n]
                answer.append(new)
        elif k < 0:
            for i in range(n):
                new = 0
                for j in range(1, abs(k)+1):
                    new += code[i - j]
                answer.append(new)
        else:
            answer = [0] * n
        return answer
