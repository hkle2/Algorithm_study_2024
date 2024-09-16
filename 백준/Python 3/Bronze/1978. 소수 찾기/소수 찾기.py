import sys

N = int(sys.stdin.readline().strip())
nums = list(map(int, sys.stdin.readline().split()))
answer = 0

for num in nums:
    if num != 1:
        check = True
        for i in range(2, num):
            if num % i == 0:
                check = False
        if check:
            answer += 1
print(answer)