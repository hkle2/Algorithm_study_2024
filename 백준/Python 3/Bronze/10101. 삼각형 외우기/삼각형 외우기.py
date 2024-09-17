import sys

angles = set()
sum_angles = 0

for _ in range(3):
    angle = int(sys.stdin.readline().strip())
    angles.add(angle)
    sum_angles += angle

if sum_angles == 180:
    if len(angles) == 1:
        print("Equilateral")
    elif len(angles) == 2:
        print("Isosceles")
    else:
        print("Scalene")
else:
    print("Error")