class Solution:
    def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
        answer = 0
        for i in range(len(arr1)):
            flag = True
            for j in range(len(arr2)):
                if abs(arr1[i]-arr2[j]) <= d:
                    flag = False
            if flag:
                answer += 1
        return answer

# class Solution:
#     def findTheDistanceValue(self, arr1: List[int], arr2: List[int], d: int) -> int:
#         answer = 0
#         for num in arr1:
#             flag = True
#             for i in range(len(arr2)):
#                 if abs(num-arr2[i]) <= d:
#                     flag = False
#             if flag:
#                 answer += 1
#         return answer