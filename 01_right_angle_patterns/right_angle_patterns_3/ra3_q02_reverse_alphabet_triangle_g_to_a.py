"""
Right Angle Patterns - 3
Q2: Reverse Alphabet Triangle (G F E ...)

Input: r
Rules:
- if r <= 0 -> "Invalid Input"
- if r > 26 -> "Invalid Row Value"

Example (r=7):
            G
          G F
        G F E
      G F E D
    G F E D C
  G F E D C B
G F E D C B A
"""

r = int(input())

if r <= 0:
    print("Invalid Input")
elif r > 26:
    print("Invalid Row Value")
else:
    for i in range(1, r + 1):
        g = 64 + r
        for j in range(1, r + 1):
            if i + j < r + 1:
                print(" ", end=" ")
            else:
                print(chr(g), end=" ")
                g -= 1
        print()
