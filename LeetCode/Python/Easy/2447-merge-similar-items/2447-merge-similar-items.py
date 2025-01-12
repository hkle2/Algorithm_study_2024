class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        count_dict = defaultdict(int)
        for value, weight in items1 + items2:
            count_dict[value] += weight
        sorted_keys = sorted(count_dict.keys())
        answer = []
        for key in sorted_keys:
            answer.append([key, count_dict[key]])
        return answer

from collections import defaultdict

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items = items1 + items2
        items_dict = defaultdict(int)
        for value, weight in items:
            items_dict[value] += weight
        return sorted(items_dict.items())

class Solution:
    def mergeSimilarItems(self, items1: List[List[int]], items2: List[List[int]]) -> List[List[int]]:
        items = items1 + items2
        items_dict = defaultdict(int)
        answer = []
        for value, weight in items:
            items_dict[value] += weight
        for key, value in items_dict.items():
            answer.append([key, value])
        return sorted(answer)