class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        answer = False
        for i in range(len(arr)-2):
            cnt = 0
            for j in range(3):
                if arr[i+j] % 2 != 0:
                    cnt += 1
            if cnt == 3:
                return True
        return answer