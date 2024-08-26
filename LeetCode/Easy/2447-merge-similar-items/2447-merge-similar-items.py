from collections import defaultdict

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