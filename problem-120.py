def expression(A, rem):
    if A %2 ==0:
        rem += A*(A - 2)
    else:
        rem += A*(A - 1)
    return rem

if __name__ == "__main__":
    rem = 0
    for i in range(3, 1001):
        rem = expression(i, rem)
    print(rem)