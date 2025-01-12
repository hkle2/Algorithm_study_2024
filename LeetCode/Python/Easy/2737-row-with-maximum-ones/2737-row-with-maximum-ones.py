class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        data = []
        for i, row in enumerate(mat):
            one_cnt = row.count(1)
            data.append([i, one_cnt])
        return sorted(data, key=lambda x: (-x[1], x[0]))[0]

class Solution:
    def rowAndMaximumOnes(self, mat: List[List[int]]) -> List[int]:
        answer = [0, 0]
        prev_cnt = 0
        for i, row in enumerate(mat):
            one_cnt = row.count(1)
            if one_cnt > prev_cnt:
                answer = [i, one_cnt]
                prev_cnt = one_cnt
        return answer

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