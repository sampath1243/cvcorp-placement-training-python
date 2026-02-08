"""
📌 Numbers - 4
Question 10:
Write a program to print the Armstrong Numbers in the Given Range.

Constraints:
- Both inputs must be > 0 else print "Invalid Inputs"
- If start > end swap
- If no armstrong numbers print "No Armstrong Numbers"

Output Format:
Armstrong Numbers in the Given Range is 1, 2, ... .

Example:
Input:
1
200
Output:
Armstrong Numbers in the Given Range is 1, 2, 3, 4, 5, 6, 7, 8, 9, 153.
"""

# ✅ Answer Code

n = int(input())
n1 = int(input())

count = 0

if n > 0 and n1 > 0:
    if n > n1:
        n, n1 = n1, n

    for i in range(n, n1 + 1):
        t = i
        c = 0
        sm = 0

        while t > 0:
            c += 1
            t //= 10

        t = i
        while t > 0:
            r = t % 10
            sm += r ** c
            t //= 10

        if sm == i:
            count += 1
            if count == 1:
                print("Armstrong Numbers in the Given Range is ", end="")
            if count > 1:
                print(end=", ")
            print(i, end="")

    if count > 0:
        print(".")
    else:
        print("No Armstrong Numbers")
else:
    print("Invalid Inputs")
