class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        answer = []
        for i in range(len(candies)):
            answer.append(candies[i] + extraCandies >= max(candies))
        return answer