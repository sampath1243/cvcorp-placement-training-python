"""
📌 Numbers - 4
Question 7:
Write a program to Calculate Power of a Number (With Pre Defined Method)

Constraints:
- If any input <= 0 print "Invalid Inputs"

Input:
First Line : base value
Second Line: exponent value

Output Format:
"<base> Power <exponent> value is <result>."

Example:
Input:
2
5
Output:
2 Power 5 value is 32.
"""

# ✅ Answer Code

b = int(input())
e = int(input())

if b > 0 and e > 0:
    pv = b ** e
    print(str(b) + " Power " + str(e) + " value is " + str(pv) + ".")
else:
    print("Invalid Inputs")
