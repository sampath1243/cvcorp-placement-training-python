"""
📌 Numbers - 6 | Question 1
Write a program to check whether Given Number is Even or Odd.
(Without  % , / , + )

Constraints:
- If input <= 0 print "InvaliD InpuT"

Example:
Input: 9  -> Output: Odd
Input: 112 -> Output: Even
"""

n=int(input())

if n<=0:
    print("InvaliD InpuT")
else:
    if int(n*0.5)*2==n:
        print("Even")
    else:
        print("Odd")
