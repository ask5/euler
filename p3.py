# Largest prime factor
# Problem 3
# The prime factors of 13195 are 5, 7, 13 and 29.
# What is the largest prime factor of the number 600851475143 ?
import math

n = 600851475143
m = 2
for i in range(2, int(math.sqrt(n))):
    if n % i == 0:
        while n % i == 0:
            n = n / i
            if i > m:
                m = i
print(m)
