class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        answer = []
        for i in range(1, len(height)):
            if height[i-1] > threshold:
                answer.append(i)
        return answer

class Solution:
    def stableMountains(self, height: List[int], threshold: int) -> List[int]:
        return [i for i in range(1, len(height)) if height[i-1] > threshold]