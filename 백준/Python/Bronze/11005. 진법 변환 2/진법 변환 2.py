import sys

N, B = map(int, sys.stdin.readline().split())
nums = "0123456789ABCDEFGHIJKLMNOPQRSTUVWXYZ"
num = ""

while N > 0:
    num += nums[N % B]
    N //= B

print(num[::-1])