"""
Hollow Patterns - 2
Q6: Double Pyramid Diamond Wings (Filled look)

Input: n
Rule: n > 0 else "Invalid Input"

Example (n=5):
    *         *
   * *       * *
  * * *     * * *
 * * * *   * * * *
* * * * * * * * * *
 * * * *   * * * *
  * * *     * * *
   * *       * *
    *         *
"""

n = int(input())

if n <= 0:
    print("Invalid Input")
else:
    # top
    for i in range(1, n + 1):
        for s in range(n - i):
            print(" ", end="")
        for j in range(i):
            print("* ", end="")
        for s in range(2 * (n - i) + 1):
            print(" ", end="")
        for j in range(i):
            print("* ", end="")
        print()

    # bottom
    for i in range(n - 1, 0, -1):
        for s in range(n - i):
            print(" ", end="")
        for j in range(i):
            print("* ", end="")
        for s in range(2 * (n - i) + 1):
            print(" ", end="")
        for j in range(i):
            print("* ", end="")
        print()
