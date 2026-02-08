"""
Q2: Print A,B alternatively for n times
Example n=5 => A,B,A,B,A,B,A,B,A,B
"""
n = int(input())
out = []
for i in range(n * 2):
    out.append("A" if i % 2 == 0 else "B")
print(",".join(out))
