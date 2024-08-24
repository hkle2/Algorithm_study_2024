import sys

T = int(sys.stdin.readline().strip())

for t in range(T):
    string = sys.stdin.readline().strip()
    print(string[0] + string[-1])