class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for num in nums:
            num_str = str(num)
            for c in num_str:
                answer.append(int(c))
        return answer

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        answer = []
        for i in nums:
            s = str(i)
            for j in s:
                answer.append(int(j))
        return answer