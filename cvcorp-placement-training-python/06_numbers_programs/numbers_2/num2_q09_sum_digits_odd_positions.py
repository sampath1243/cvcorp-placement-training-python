"""
📌 Question 9: Sum of Digits at Odd Positions

Write a Program to Find Sum of Digits which are in Odd Positions in a Given Number.

Odd Position means:
- Count from RIGHT SIDE
- Position 1, 3, 5, 7...

Constraints:
- Given Input Must be Greater than Zero, else Print Invalid Input.

Input:
First Line of Input Consists of One Integer Value.

Output:
Print sum of digits in odd positions.

Example:
Input:
2568
Positions from right:
8(1st), 6(2nd), 5(3rd), 2(4th)
Odd positions digits: 8 + 5 = 13

Output:
13
"""

# ✅ Answer Code

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    pos = 1
    total = 0
    temp = n

    while temp > 0:
        d = temp % 10
        if pos % 2 == 1:
            total += d
        pos += 1
        temp //= 10

    print(total)
