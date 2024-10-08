class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        answer = []
        leftSum = [0]
        rightSum = []
        left, right = 0, 0
        for i in range(len(nums)-1):
            left += nums[i]
            leftSum.append(left)
        for i in range(1, len(nums)):
            right = sum(nums[i:])
            rightSum.append(right)
        rightSum.append(0)
        for a, b in zip(leftSum, rightSum):
            answer.append(abs(a - b))
        return answer