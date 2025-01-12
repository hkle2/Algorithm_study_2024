class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        answer = []
        for n, i in zip(nums, index):
            answer.insert(i, n)
        return answer