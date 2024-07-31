class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(k):
            gifts = sorted(gifts)
            max_gifts = gifts.pop()
            gifts.append(int(math.sqrt(max_gifts)))
        return sum(gifts)

class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        answer = 0
        for i in range(k):
            gifts.sort(reverse=True)
            gifts[0] = int(gifts[0]**0.5)
        answer = sum(gifts)
        return answer