class Solution:
    def clearDigits(self, s: str) -> str:
        # while, 숫자를 지울 수 있는 조건 잘 살펴보기
        while s:
            flag = False
            # 첫 번째 숫자 찾아서 제거
            # 숫자 제거, 문자열 slicing 활용
            # 3번째 위치한 문자를 제거
            # s = s[:3] + s[4:]
            for i, c in enumerate(s):
                if c.isnumeric():
                    flag = True
                    if i == 0:
                        s = s[i+1:]
                    else:
                        s = s[:i-1] + s[i+1:]
                    break
            if not flag:
                break
        return s

# class Solution:
#     def clearDigits(self, s: str) -> str:
#         answer = []
#         for i in s:
#             if i.isdigit():
#                 answer.pop()
#             else:
#                 answer.append(i)
#         return "".join(answer)
