"""
Q6: Biggest among 3 numbers
Output: "<max> is a Biggest Number from the Given Numbers"
"""
a = int(input())
b = int(input())
c = int(input())

m = a
if b > m:
    m = b
if c > m:
    m = c

print(m, "is a Biggest Number from the Given Numbers")
