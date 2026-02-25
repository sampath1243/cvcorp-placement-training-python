"""
📌 Numbers - 6 | Question 3
Write a program to check whether given number is even or odd.
(Without  % , / , + , * )

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
    if n&1 == 0:
        print("Even")
    else:
        print("Odd")
