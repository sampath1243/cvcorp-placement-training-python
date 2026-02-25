"""
Q3:
If n not in 0..100 -> "INVALID INPUT"
91-100 -> SUPER SMART
81-90 -> SMART
71-80 -> SMART ENOUGH
61-70 -> JUST SMART
36-60 -> NO SMART
0-35 -> DUMB
"""
n = int(input())

if n < 0 or n > 100:
    print("INVALID INPUT")
elif 91 <= n <= 100:
    print("SUPER SMART")
elif 81 <= n <= 90:
    print("SMART")
elif 71 <= n <= 80:
    print("SMART ENOUGH")
elif 61 <= n <= 70:
    print("JUST SMART")
elif 36 <= n <= 60:
    print("NO SMART")
else:
    print("DUMB")
