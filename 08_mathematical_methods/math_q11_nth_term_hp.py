"""
Question 11:
Find the nth term value in the Harmonic progression series.

Constraints:
n must be > 0 else print "InvaliD InPut"
Output must be in %.2f format
"""

a = int(input())
d = int(input())
n = int(input())

if n <= 0:
    print("InvaliD InPut")
else:
    ap = a + (n - 1) * d
    hp = 1 / ap
    print("%.2f" % hp)
