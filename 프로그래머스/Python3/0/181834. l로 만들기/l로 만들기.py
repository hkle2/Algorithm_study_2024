# def solution(myString):
#     answer = ''
#     for i in myString:
#         if i < "l":
#             answer += "l"
#         else:
#             answer += i
#     return answer

def solution(myString):
    answer = myString.translate(myString.maketrans('abcdefghijk', 'lllllllllll'))
    return answer