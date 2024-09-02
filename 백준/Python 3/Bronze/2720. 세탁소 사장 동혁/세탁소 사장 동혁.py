import sys

T = int(sys.stdin.readline().strip())

for _ in range(T):
    answer = []
    C = int(sys.stdin.readline().strip())
    for change in [25, 10, 5, 1]:
        print(C // change, end=" ")
        C %= change
    print()