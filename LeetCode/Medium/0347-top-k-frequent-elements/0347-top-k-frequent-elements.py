from collections import Counter
class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        num_dict = Counter(nums)
        nums_dict = dict(sorted(num_dict.items(), key=lambda x: x[1], reverse=True))
        for i, (key, value) in enumerate(nums_dict.items()):
            if i < k:
                answer.append(key)
        return answer
        