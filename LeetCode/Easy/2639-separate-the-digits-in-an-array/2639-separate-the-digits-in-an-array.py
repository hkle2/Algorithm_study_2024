class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            s = str(i)
            for j in range(len(s)):
                answer.append(int(s[j]))
        return answer
        