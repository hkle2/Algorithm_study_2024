import sys

nums = sys.stdin.readline().strip()
dial = {2: ["A", "B", "C"], 3: ["D", "E", "F"], 4: ["G", "H", "I"], 5: ["J", "K", "L"], 6: ["M", "N", "O"], 7: ["P", "Q", "R", "S"], 8: ["T", "U", "V"], 9: ["W", "X", "Y", "Z"]}
answer = 0

for num in nums:
    for n, d in dial.items():
        if num in d:
            answer += n+1

print(answer)