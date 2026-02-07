"""
Right Angle Patterns - 3
Q5: Alternate Row Symbols (% and &) in decreasing triangle

Input: n
Constraint: n > 0 else "Invalid Input"

Example (n=5):
% % % % %
& & & &
% % %
& &
%
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    for i in range(n, 0, -1):
        sym = "%" if i % 2 == 1 else "&"
        for j in range(i):
            print(sym, end=" ")
        print()
