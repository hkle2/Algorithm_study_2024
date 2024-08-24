import sys

pieces1 = [1, 1, 2, 2, 2, 8]
pieces2 = list(map(int, sys.stdin.readline().split()))
pieces = []

for i in range(len(pieces1)):
    pieces.append(pieces1[i] - pieces2[i])

for piece in pieces:
    print(piece, end=" ")