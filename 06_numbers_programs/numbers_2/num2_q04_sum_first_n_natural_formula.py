"""
📌 Question 4: Sum of N Natural Numbers using Formula

Write a Program to Find Sum of N Natural Numbers using Formula.

Constraints:
- If Input is 0, Print InvaLid Input.
- If Input is Negative, Print:
  "Sorry! you have Entered Negative Values."

Input:
First Line of Input Consists of One Integer Value.

Output:
Print Sum of N Natural Numbers.

Example 1:
Input:
5
Output:
Sum of 'N' Natural Numbers is 15.

Example 2:
Input:
-5
Output:
Sorry! you have Entered Negative Values.

Example 3:
Input:
0
Output:
InvaLid Input.
"""

# ✅ Answer Code

n = int(input())

if n == 0:
    print("InvaLid Input.")
elif n < 0:
    print("Sorry! you have Entered Negative Values.")
else:
    total = n * (n + 1) // 2
    print(f"Sum of 'N' Natural Numbers is {total}.")
