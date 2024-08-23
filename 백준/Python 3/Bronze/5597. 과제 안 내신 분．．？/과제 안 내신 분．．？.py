import sys

nums = [n for n in range(1, 31)]

for i in range(28):
    nums.remove(int(sys.stdin.readline().strip()))

for num in nums:
    print(num)