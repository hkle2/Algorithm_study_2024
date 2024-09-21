class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        answer = 0
        for i in range(len(accounts)):
            answer = max(sum(accounts[i]), answer)
        return answer