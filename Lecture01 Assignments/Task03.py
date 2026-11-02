#Write a program that asks the user for the length and width of a rectangle. The program then prints out the perimeter and area of the rectangle. The perimeter of a rectangle is the sum of the lengths of all four sides.
Length=float(input("Enter the length of a rectangle: "))
Width=float(input("Enter the width of a rectangle: "))
perimeter=2 * (Length+Width)
area=Length*Width
print(f"Perimeter of the rectangle: {perimeter}")
print(f"Area of the rectangle: {area}")