class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        answer = []
        for i in range(len(mountain)):
            if i == 0 or i == len(mountain) - 1:
                continue
            if mountain[i] < mountain[i-1] and mountain[i] > mountain[i+1]:
                answer.append(i)
        return answer

class Solution:
    def findPeaks(self, mountain: List[int]) -> List[int]:
        answer = []
        for i in range(1, len(mountain)-1):
            if mountain[i-1] < mountain[i] and mountain[i] > mountain[i+1]:
                answer.append(i)
        return answer
