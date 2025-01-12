class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        nums_dict = {}
        for num in nums:
            if num not in nums_dict:
                nums_dict[num] = 0
            nums_dict[num] += 1
        sorted_keys = sorted(nums_dict, key=lambda x: nums_dict[x], reverse=True)
        for i in range(k):
            answer.append(sorted_keys[i])
        return answer

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        nums_counter = Counter(nums)
        return [x[0] for x in nums_counter.most_common()[:k]]

from collections import Counter

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        answer = []
        num_dict = Counter(nums)
        count = sorted(num_dict.items(), key=lambda x: x[1], reverse=True)
        for i in range(k):
            answer.append(count[i][0])
        return answer