def solution(ineq, eq, n, m):
    answer = 0
    if n > m:
        if (ineq == ">" and eq == "=") or (ineq == ">" and eq == "!"):
            answer = 1
    elif n < m:
        if (ineq == "<" and eq == "=") or (ineq == "<" and eq == "!"):
            answer = 1
    else:
        if (ineq == ">" and eq == "=") or (ineq == "<" and eq == "="):
            answer = 1
    return answer