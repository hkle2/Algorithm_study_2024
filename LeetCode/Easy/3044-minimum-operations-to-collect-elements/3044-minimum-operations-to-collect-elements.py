class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        collections = set()
        target = set([x + 1 for x in range(k)])
        while nums:
            poped_num = nums.pop()
            collections.add(poped_num)
            answer += 1
            # target이 collections안에 모두 포함되는 경우, break
            # set intersection을 사용
            if target.intersection(collections) == target:
                break
        return answer

# class Solution:
#     def minOperations(self, nums: List[int], k: int) -> int:
#         answer = 0
#         collection = set()
#         for i, n in enumerate(reversed(nums)):
#             if n > k:
#                 continue
#             collection.add(n)
#             if len(collection) == k:
#                 return i + 1