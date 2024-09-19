class Solution:
    def circularGameLosers(self, n: int, k: int) -> List[int]:
        cur_loc = 0
        friends = [0]
        i = 1
        while True:
            cur_loc = (cur_loc + i * k) % n
            if cur_loc not in friends:
                friends.append(cur_loc)
                i += 1
            else:
                break
        print(friends)
        answer = []
        for i in range(n):
            if i not in friends:
                answer.append(i+1)
        return answer