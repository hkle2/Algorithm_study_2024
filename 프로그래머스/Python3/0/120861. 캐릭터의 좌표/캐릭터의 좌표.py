def solution(keyinput, board):
    answer = []
    x, y = 0, 0
    a, b  = 0, 0
    w, l = board[0] // 2, board[1] // 2
    move = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    for i in keyinput:
        a += move[i][0]
        b += move[i][1]
        if -w <= a <= w and -l <= b <= l:
            x += move[i][0]
            y += move[i][1]
        else:
            a -= move[i][0]
            b -= move[i][1]
    answer.append(x)
    answer.append(y)
    return answer

def solution(keyinput, board):
    answer = []
    x, y = 0, 0
    w, l = board[0] // 2, board[1] // 2
    move = {"up": (0, 1), "down": (0, -1), "left": (-1, 0), "right": (1, 0)}
    for i in keyinput:
        dx, dy = move[i]
        if w < abs(x + dx) or l < abs(y + dy):
            continue
        else:
            x, y = x + dx, y + dy
    answer.append(x)
    answer.append(y)
    return answer