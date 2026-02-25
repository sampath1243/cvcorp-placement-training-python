"""
📌 Numbers - 4
Question 5:
Write a Program to Check if The given year is Leap Year or not?

Constraints:
- Year must be greater than 0
- Else print "Given Year is Invalid Input."

Output:
- If leap year -> "Leap Year."
- Else -> "Not a Leap Year."

Example 1:
Input:
2024
Output:
Leap Year.

Example 2:
Input:
2023
Output:
Not a Leap Year.
"""

# ✅ Answer Code

year = int(input())

if year <= 0:
    print("Given Year is Invalid Input.")
else:
    if year % 400 == 0 or (year % 4 == 0 and year % 100 != 0):
        print("Leap Year.")
    else:
        print("Not a Leap Year.")
