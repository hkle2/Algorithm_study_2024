import sys

nums = sys.stdin.readline().strip()
dial = ["ABC", "DEF", "GHI", "JKL", "MNO", "PQRS", "TUV", "WXYZ"]
answer = 0

for num in nums:
    for i in range(len(dial)):
        if num in dial[i]:
            answer += i+3

print(answer)