"""
There are exactly ten ways of selecting three from five, 12345:

123, 124, 125, 134, 135, 145, 234, 235, 245, and 345

In combinatorics, we use the notation, (53)=10

.

In general, (nr)=n!r!(n−r)!
, where r≤n, n!=n×(n−1)×...×3×2×1, and 0!=1

.

It is not until n=23
, that a value exceeds one-million: (2310)=1144066

.

How many, not necessarily distinct, values of (nr)
for 1≤n≤100, are greater than one-million?

"""

def factorial(n):
    if n == 0 or n == 1:
        return 1
    else:
        return n * factorial(n-1)

def combinations(n, r, Arr):
    final_val = factorial(n)/(factorial(r)*factorial(n-r))
    if final_val > 1000000:
        Arr.append((n,r))
    return Arr

if __name__ == "__main__":
    Arr = []
    for i in range(1, 101):
        for j in range(1, i):
            Arr = combinations(i, j, Arr)
    print(len(Arr))