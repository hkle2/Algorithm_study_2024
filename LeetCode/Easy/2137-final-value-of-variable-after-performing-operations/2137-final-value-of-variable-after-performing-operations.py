class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for operation in operations:
            # X++ 혹은 ++X일 때는 +1
            # 아니면 -1
            if operation == "++X" or operation == "X++":
                answer += 1
            else:
                answer -= 1
        return answer

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        answer = 0
        for i in operations:
            if "+" in i:
                answer += 1
            else:
                answer -= 1
        return answer