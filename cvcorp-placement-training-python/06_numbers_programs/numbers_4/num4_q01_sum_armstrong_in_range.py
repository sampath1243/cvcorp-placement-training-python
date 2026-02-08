"""
📌 Numbers - 4
Question 1:
Write a program to print the Sum of the Armstrong Numbers in the Given Range?

Constraints:
- Either of the given inputs is equal to zero then print "Invalid Inputs"
- If there is no Armstrong values in the given range then print:
  "No Armstrong Numbers in a Given Range."
- If any input is negative convert to positive
- If first value > second value swap

Input:
First Line : Start Value
Second Line: End Value

Output:
Armstrong Numbers in the Given Range is 1 + 2 + ... = SUM.

Example:
Input:
100
500
Output:
Armstrong Numbers in the Given Range is 153 + 370 + 371 + 407 = 1301.
"""

# ✅ Answer Code

n = int(input())
n1 = int(input())

arm_sum = 0
count = 0

if n == 0 or n1 == 0:
    print("Invalid Inputs")
else:
    if n < 0:
        n = -n
    if n1 < 0:
        n1 = -n1
    if n > n1:
        n, n1 = n1, n

    for i in range(n, n1 + 1):
        t = i
        dc = 0
        s = 0

        while t > 0:
            t //= 10
            dc += 1

        t = i
        while t > 0:
            r = t % 10
            s = s + r ** dc
            t //= 10

        if s == i:
            count += 1
            if count == 1:
                print("Armstrong Numbers in the Given Range is ", end="")
            if count > 1:
                print(end=" + ")
            print(i, end="")
            arm_sum += i

    if count > 0:
        print(" =", arm_sum, end=".")
    else:
        print("No Armstrong Numbers in a Given Range.")
