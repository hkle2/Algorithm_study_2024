class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        # 3중 for문 사용
        answer = 0
        for i in range(len(arr)):
            for j in range(i+1, len(arr)):
                if abs(arr[i] - arr[j]) > a:
                    continue
                for k in range(j+1, len(arr)):
                    # |arr[i] - arr[j]| <= a
                    # |arr[j] - arr[k]| <= b
                    # |arr[i] - arr[k]| <= c
                    # 세 가지 조건을 모두 충족하면 answer에 1 더해주기
                    if abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
                        answer += 1
        return answer

# class Solution:
#     def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
#         answer = 0
#         for i in range(len(arr)):
#             for j in range(i+1, len(arr)):
#                 for k in range(j+1, len(arr)):
#                     if abs(arr[i] - arr[j]) <= a and abs(arr[j] - arr[k]) <= b and abs(arr[i] - arr[k]) <= c:
#                         answer += 1
#         return answer