class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        element = set()
        for num in nums:
            if num > 0:
                element.add(num)
        return len(element)

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len({num for num in nums if num})

class Solution:
    def minimumOperations(self, nums: List[int]) -> int:
        return len(set(filter(lambda x: x > 0, nums)))