import sys

ori_pieces = [1, 1, 2, 2, 2, 8]
cur_pieces = list(map(int, sys.stdin.readline().split()))

for i in range(len(ori_pieces)):
    print(ori_pieces[i] - cur_pieces[i], end=" ")