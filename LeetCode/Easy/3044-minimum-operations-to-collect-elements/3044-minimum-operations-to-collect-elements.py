class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        answer = 0
        collection = set()
        for i, n in enumerate(reversed(nums)):
            print(i, n)
            if n > k:
                continue
            collection.add(n)
            if len(collection) == k:
                return i + 1