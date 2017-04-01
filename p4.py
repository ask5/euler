# Largest palindrome product
# Problem 4
# A palindromic number reads the same both ways. The largest palindrome made from the product of
# two 2-digit numbers is 9009 = 91 × 99.
# Find the largest palindrome made from the product of two 3-digit numbers.

def is_palindrome(n):
    t = n
    rev = 0
    while t > 0:
        rev = rev * 10 + t % 10
        t = int(t / 10)
    if n == rev:
        return True
    else:
        return False

m = 0
for n1 in range(999, 100, -1):
    for n2 in range(999, 100, -1):
        t = n1 * n2
        if is_palindrome(t):
            if (t) > m:
                m = t

print(m)
