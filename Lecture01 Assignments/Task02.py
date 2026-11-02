#Write a program that asks the user for the radius of a circle and then prints out the area with two decimals of the circle.
import math
radius=float(input("Please enter the radius of a circle: "))
area=math.pi * radius ** 2
print(f"The area of the circle is: {area:.2f}")