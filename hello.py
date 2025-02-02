def minimumOfthree(a, b, c):
    if a <= b and a <= c:
        return a
    elif b <= a and b <= c:
        return b
    else:
        return c

# Function call
result = minimumOfthree(11, 23, 12)
print("Minimum value is:", result)
