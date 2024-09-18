import sys

N = int(sys.stdin.readline().strip())
nums = []

for _ in range(N):
    nums.append(int(sys.stdin.readline().strip()))
nums.sort()

for num in nums:
    print(num)