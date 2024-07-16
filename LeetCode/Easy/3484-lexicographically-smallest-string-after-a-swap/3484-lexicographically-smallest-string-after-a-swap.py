class Solution:
    def getSmallestString(self, s: str) -> str:
        # 1. 반복문을 돌면서 인접한 두 글자가 모두 짝수이거나 모두 홀수인 경우를 찾는다. -> O
        # 2. swap을 수행해서 새로운 문자열을 만든다. -> O
        # 3. 새로 만든 문자열을 candidates라는 list에 추가한다.
        # 4. candidates를 정렬한 다음, 가장 앞에 오는 수를 리턴한다.
        answer = [s]
        for i in range(len(s) - 1):
            if int(s[i]) % 2 == int(s[i+1]) % 2:
                swaped = s[:i] + s[i+1] + s[i] + s[i+2:]
                answer.append(swaped)
        return sorted(answer)[0]

# class Solution:
#     def getSmallestString(self, s: str) -> str:
#         for i in range(len(s)-1):
#             a, b = int(s[i]), int(s[i+1])
#             if a % 2 == b % 2 and a < b:
#                 return s[:i] + s[i+1] + s[i] + s[i+2:]
#         return s

# class Solution:
#     def getSmallestString(self, s: str) -> str:
#         l = list(s)
#         answer = []
#         for i in range(len(l)-1):
#             a, b = int(l[i]), int(l[i+1])
#             if (a % 2 == 0 and b % 2 == 0) or (a % 2 != 0 and b % 2 != 0):
#                 l[i], l[i+1] = l[i+1], l[i]
#                 answer.append("".join(l))
#         answer.sort(reverse=True)
#         if len(answer) == 0:
#             return s
#         else:
#             return answer[0]