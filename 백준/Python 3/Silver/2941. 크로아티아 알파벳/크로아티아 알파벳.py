import sys

cro_alphas = ["c=", "c-", "dz=", "d-", "lj", "nj", "s=", "z="]
s = sys.stdin.readline().strip()

for cro_alpha in cro_alphas:
    s = s.replace(cro_alpha, "a")

print(len(s))