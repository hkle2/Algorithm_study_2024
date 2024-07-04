class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        answer = []
        for i in mat:
            cnt = 0
            for j in i:
                if j == 1:
                    cnt += 1
            answer.append(cnt)
        n = answer.index(max(answer))
        m = max(answer)
        return [n, m]