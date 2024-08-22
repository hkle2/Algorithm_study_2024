class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        answer = 0
        for command in commands:
            if command == "UP":
                answer -= n
            elif command == "RIGHT":
                answer += 1
            elif command == "DOWN":
                answer += n
            else:
                answer -= 1
        return answer
