#Write a program that generates two random combinations of numbers for a combination lock:
#A 3-digit code where each number is between 0 and 9.
#A 4-digit code where each number is between 1 and 6.

import random
code1 = random.randint(0, 9), random.randint(0, 9), random.randint(0, 9)
code2 = random.randint(1, 6), random.randint(1, 6), random.randint(1, 6), random.randint(1, 6)
print(f"The 3-digit code where each number is between 1 and 6:", *code1)
print(f"The 4-digit code where each number is between 1 and 6:", *code2)