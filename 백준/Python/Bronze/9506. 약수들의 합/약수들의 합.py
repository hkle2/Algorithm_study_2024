import sys

answer = []

while True:
    n = int(sys.stdin.readline().strip())
    if n == -1:
        break
    for i in range(1, n):
        if n % i == 0:
            answer.append(i)
    if sum(answer) == n:
        print(f"{n} = ", end="")
        for i in range(len(answer)-1):
            print(f"{answer[i]} + ", end="")
        print(f"{answer[-1]}")
    else:
        print(f"{n} is NOT perfect.")
    answer = []