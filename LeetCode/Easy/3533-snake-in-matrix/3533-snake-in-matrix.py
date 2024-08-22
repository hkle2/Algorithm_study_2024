class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        c = Counter(commands)
        move_y = c['DOWN'] - c['UP']
        move_x = c['RIGHT'] - c['LEFT']
        answer = move_y * n  +move_x
        return answer

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
