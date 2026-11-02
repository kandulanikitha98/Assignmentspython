#Write a program that asks the user for three integer numbers. The program prints out the sum, product, and average of the numbers
a=int(input("Please enter a number: "))
b=int(input("Please enter a number: "))
c=int(input("Please enter a number: "))
sum=a+b+c
print(f"The sum of Numbers: {sum}")
product=a*b*c
print(f"The product of Numbers: {product}")
average=(a+b+c)/3
print(f"The average of three numbers: {average}")