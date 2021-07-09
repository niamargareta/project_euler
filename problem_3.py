"""The prime factors of 13195 are 5, 7, 13 and 29.

What is the largest prime factor of the number 600851475143 ?"""


def is_prime(y):
    for x in range(2, y):
        if (y/x).is_integer():
            return False
    return True


for x in range(2, 13195):
    if (13195/x).is_integer():
        if is_prime(x):
            print(x)
