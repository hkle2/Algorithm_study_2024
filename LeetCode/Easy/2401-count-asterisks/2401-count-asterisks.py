class Solution:
    def countAsterisks(self, s: str) -> int:
        # split, count, for, if
        answer = 0
        word_list = s.split("|")
        for i in range(0, len(word_list), 2):
            # word_list[i] 안에 포함되어 있는 *의 개수 세어서
            # answer에다가 추가하기
            answer += word_list[i].count("*")
        return answer

# class Solution:
#     def countAsterisks(self, s: str) -> int:
#         answer = 0
#         l = s.split("|")
#         for i in range(0, len(l)+1, 2):
#             answer += l[i].count("*")
#         return answer