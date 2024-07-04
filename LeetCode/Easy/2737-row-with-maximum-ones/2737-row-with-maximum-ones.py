class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        answer = []
        for i in mat:
            cnt = 0
            for j in i:
                if j == 1:
                    cnt += 1
            answer.append(cnt)
        m = answer.index(max(answer))
        n = max(answer)
        return [m, n]