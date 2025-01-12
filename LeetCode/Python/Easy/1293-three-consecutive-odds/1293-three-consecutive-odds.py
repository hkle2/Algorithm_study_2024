class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        answer = False
        for i in range(len(arr)-2):
            if arr[i] % 2 == 1 and arr[i + 1] % 2 == 1 and arr[i + 2] % 2 == 1:
                answer = True
                break
        return answer

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        answer = False
        cnt = 0
        for num in arr:
            # 만약 현재 숫자가 짝수라면 여기서부터는 연속된 홀수가 0
            # 만약 현재 숫자가 홀수라면 직전 홀수 개수 + 1만큼 연속된 홀수가 있는 것
            # 만약 연속된 홀수가 3개 이상 등장한다면 answer를 True로 놓고 break
            if num in arr:
                if num % 2 == 0:
                    cnt = 0
                else:
                    cnt += 1
            if cnt >= 3:
                answer = True
                break
        return answer

class Solution:
    def threeConsecutiveOdds(self, arr: List[int]) -> bool:
        for i in range(len(arr)-2):
            cnt = 0
            for j in range(3):
                if arr[i + j] % 2 != 0:
                    cnt += 1
            if cnt == 3:
                return True
        return False