from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        num_dict = Counter(nums)
        count = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            answer.append(count[i][0])
        return answer