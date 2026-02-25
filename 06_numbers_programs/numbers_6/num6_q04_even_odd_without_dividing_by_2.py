"""
📌 Numbers - 6 | Question 4
Write a program to check whether given number is even or odd.
(Without dividing by 2)

Constraints:
- If input <= 0 print "Invalid Input"

Example:
Input: 92 -> Even
Input: 11 -> Odd
"""

n=int(input())

if n<=0:
    print("Invalid Input")
else:
    if n^1 > n:
        print("Even")
    else:
        print("Odd")
