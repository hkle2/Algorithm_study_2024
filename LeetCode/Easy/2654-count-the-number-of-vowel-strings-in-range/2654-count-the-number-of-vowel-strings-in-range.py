class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        # for, in
        vowels = ["a", 'e', 'i', 'o', 'u']
        answer = 0
        for i in range(left, right + 1):
            word = words[i]
            # word의 각 글자를 반복하면서 모음인지 체크하고
            # 모음이면 answer에 1 더해주기
            if word[0] in vowels and word[-1] in vowels:
                answer += 1
        return answer

# class Solution:
#     def vowelStrings(self, words: List[str], left: int, right: int) -> int:
#         answer = 0
#         vowels = "aeiou"
#         for i in range(left, right+1):
#             if words[i][0] in vowels and words[i][-1] in vowels:
#                 answer += 1
#         return answer