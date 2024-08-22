import sys

N, X = map(int, sys.stdin.readline().split(" "))

for i in list(map(int, sys.stdin.readline().split(" "))):
    if i < X:
        print(i, end=" ")