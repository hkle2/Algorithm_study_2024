class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        answer = 0
        for arr in arr1:
            flag = True
            for i in range(len(arr2)):
                if abs(arr-arr2[i]) <= d:
                    flag = False
            if flag:
                answer += 1
        return answer