"""
📌 Question 8: Sum of N Natural Numbers without Formula

Write a Program to Find Sum of N Natural Numbers without using Formula.

Constraints:
- If Input is 0, Print InvaLid Input.
- If Input is Negative, Print:
  "Sorry! you have Entered Negative Values."

Input:
First Line of Input Consists of One Integer Value.

Output:
Print full series and total sum.

Example:
Input:
5
Output:
Sum of 'N' Natural Numbers is 1 + 2 + 3 + 4 + 5 = 15.
"""

# ✅ Answer Code

n = int(input())

if n == 0:
    print("InvaLid Input.")
elif n < 0:
    print("Sorry! you have Entered Negative Values.")
else:
    total = 0
    parts = []

    for i in range(1, n + 1):
        total += i
        parts.append(str(i))

    series = " + ".join(parts)
    print(f"Sum of 'N' Natural Numbers is {series} = {total}.")
