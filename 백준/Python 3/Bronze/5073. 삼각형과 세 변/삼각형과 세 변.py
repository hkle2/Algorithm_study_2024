import sys

while True:
    angles = []
    a, b, c = map(int, sys.stdin.readline().split())
    if a == 0 and b == 0 and c == 0:
        break
    angles.append(a)
    angles.append(b)
    angles.append(c)
    angles.sort()
    if angles[2] >= angles[0] + angles[1]:
        print("Invalid")
    elif len(set(angles)) == 1:
        print("Equilateral")
    elif len(set(angles)) == 2:
        print("Isosceles")
    else:
        print("Scalene")